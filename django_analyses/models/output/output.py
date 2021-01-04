from django.db import models
from model_utils.managers import InheritanceManager
from typing import Any


class Output(models.Model):
    run = models.ForeignKey(
        "django_analyses.Run",
        on_delete=models.CASCADE,
        related_name="base_output_set",
    )

    value = None
    definition = None

    objects = InheritanceManager()

    class Meta:
        ordering = ("run",)

    def __str__(self) -> str:
        return f"'{self.key}' = {self.value}"

    def pre_save(self) -> None:
        pass

    def validate(self) -> None:
        pass

    def save(self, *args, **kwargs):
        self.pre_save()
        self.validate()
        super().save(*args, **kwargs)

    def get_json_value(self) -> Any:
        return self.value.id if self.value_is_foreign_key else self.value

    @property
    def key(self) -> str:
        if self.definition:
            return self.definition.key

    @property
    def json_value(self) -> Any:
        return self.get_json_value()

    @property
    def value_is_foreign_key(self) -> bool:
        value_field = self._meta.get_field("value")
        return isinstance(value_field, models.ForeignKey)
