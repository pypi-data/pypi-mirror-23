"""The actual Bucket ODM model itself."""

from jacquard.odm import Model, ListField, EncodeDecodeField

from .entry import _Entry, _decode_entry, _encode_entry


class Bucket(Model):
    """A single partition of user space, with associated settings."""

    entries = ListField(null=False, field=EncodeDecodeField(
        encode=_encode_entry,
        decode=_decode_entry,
        null=False,
        default=[],
    ), default=())

    def get_settings(self, user_entry):
        """Look up settings by user entry."""
        settings = {}

        for entry in self.entries:
            if (
                not entry.constraints or
                entry.constraints.matches_user(user_entry)
            ):
                settings.update(entry.settings)

        return settings

    def affected_settings(self):
        """All settings determined in this bucket."""
        return frozenset(
            y
            for x in self.entries
            for y in x.settings.keys()
        )

    def needs_constraints(self):
        """Whether any settings in this bucket involve constraint lookups."""
        return any(x.constraints for x in self.entries)

    def add(self, key, settings, constraints):
        """Add a new, keyed entry."""
        self.entries = self.entries + (_Entry(
            key=key,
            settings=settings,
            constraints=constraints,
        ),)
        self.mark_dirty()

    def remove(self, key):
        """Remove any matching, keyed entry."""
        self.entries = [
            x
            for x in self.entries
            if x.key != key
        ]
        self.mark_dirty()

    def covers(self, key):
        """Whether a given key is covered under this bucket."""
        return any(
            x.key == key
            for x in self.entries
        )
