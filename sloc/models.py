from django.db import models

class Segment(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    directory_path_used = models.CharField(max_length=200)
    def __unicode__(self):
        return u"%s (%s)" % (unicode(self.name),unicode(self.branch))

class Language(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __unicode__(self):
        return u"%s (%s)" % (unicode(self.name),unicode(self.description))

class SlocType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __unicode__(self):
        return u"%s" % (unicode(str(self.name)))

class Sloc(models.Model):
    source_lines_of_code = models.IntegerField()
    generated_date = models.DateTimeField('date generated')
    created_date = models.DateTimeField(auto_now=True, editable=False)
    segment = models.ForeignKey(Segment)
    language = models.ForeignKey(Language)
    reported_by = models.CharField(max_length=200)
    sloc_type = models.ForeignKey(SlocType)
    def __unicode__(self):
        return u"%s" % (unicode(str(self.source_lines_of_code)))
