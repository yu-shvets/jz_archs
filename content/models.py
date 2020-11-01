from django.db import models
import datetime
from django.utils.text import slugify


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Project(CommonInfo):

    YEAR_CHOICES = [(str(r), str(r)) for r in range(2006, datetime.date.today().year+1)]

    class Meta(CommonInfo.Meta):
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ('position',)

    name = models.CharField(max_length=256)
    main_image = models.ImageField(blank=True, null=True, upload_to='projects/main_images')
    year = models.CharField(max_length=4, blank=True, choices=YEAR_CHOICES)
    info = models.TextField(blank=True, default='')
    slug = models.SlugField(blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, default=1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)


class Image(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Image"
        verbose_name_plural = "Images"

    image = models.ImageField(upload_to='projects/images')
    position = models.PositiveIntegerField(blank=True, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.project, self.image)


class About(models.Model):

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    photo = models.ImageField(blank=True, null=True, upload_to='about/photo')
    info = models.TextField()

    def __str__(self):
        return 'info'


class WorkListCommonInfo(models.Model):
    years = models.CharField(max_length=16)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.years


class WorkExperienceWorkList(WorkListCommonInfo):

    class Meta(WorkListCommonInfo.Meta):
        verbose_name = 'Worklist - Work Experience'
        verbose_name_plural = 'Worklist - Work Experience'


class ProjectsWorkList(WorkListCommonInfo):

    class Meta(WorkListCommonInfo.Meta):
        verbose_name = 'Worklist - Project'
        verbose_name_plural = 'Worklist - Projects'


class WorkshopsWorkList(WorkListCommonInfo):

    class Meta(WorkListCommonInfo.Meta):
        verbose_name = 'Worklist - Workshop'
        verbose_name_plural = 'Worklist - Workshops'
