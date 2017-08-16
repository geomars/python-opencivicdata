from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.encoding import python_2_unicode_compatible

from ...common import JURISDICTION_CLASSIFICATION_CHOICES
from .base import OCDBase, OCDIDField
from .division import Division


@python_2_unicode_compatible
class Jurisdiction(OCDBase):
    id = OCDIDField(ocd_type='jurisdiction')
    name = models.CharField(
        max_length=300,
        help_text="The common name of the Jurisdiction, such as 'Wyoming' or 'Hope County School System.'"
    )
    url = models.URLField(
        max_length=2000,
        help_text="The primary website of the Jurisdiction."
    )
    classification = models.CharField(
        max_length=50,
        choices=JURISDICTION_CLASSIFICATION_CHOICES,
        default='government',
        db_index=True,
        help_text="The type of jurisdiction being defined."
    )
    feature_flags = ArrayField(
        base_field=models.TextField(),
        blank=True,
        default=list,
        help_text="A list of features that are present for data in this jurisdiction."
    )
    division = models.ForeignKey(
        Division,
        related_name='jurisdictions',
        db_index=True,
        help_text="A link to a Division related to this Jurisdiction."
    )

    class Meta:
        db_table = 'opencivicdata_jurisdiction'

    def __str__(self):
        return self.name
