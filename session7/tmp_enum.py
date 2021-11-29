class Snapshot(models.Model):
    SNAPSHOT_COLLECTING = 'collecting data'
    SNAPSHOT_HAS_DATA = 'has data'
    SNAPSHOT_DELETED = 'deleted'

    SNAPSHOT_STATUS = (
        (SNAPSHOT_COLLECTING, 'collecting data',),
        (SNAPSHOT_HAS_DATA, 'has data',),
        (SNAPSHOT_DELETED, 'deleted',),
    )

    name = models.CharField(max_length=64, default="Feature/R2R",
                            null=True, editable=False)
    date = models.DateTimeField(auto_now=True, null=False, blank=True,
                                editable=False)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=64, choices=SNAPSHOT_STATUS,
                              default=SNAPSHOT_COLLECTING,
                              null=True, blank=True)

    class Meta:
        verbose_name = _('Snapshot')
        verbose_name_plural = _('Snapshots')