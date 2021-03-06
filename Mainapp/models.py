from django.db import models


class customer(models.Model):
    cu_id = models.CharField(max_length=45, null=False, primary_key=True)
    pw = models.CharField(max_length=45, null=False)
    name = models.CharField(max_length=45, null=False)
    phone = models.CharField(max_length=45, null=False)
    profile = models.FileField(upload_to="profile/")

    class Meta:
        db_table = 'customer'
        managed = False


class counselor(models.Model):
    co_id = models.CharField(max_length=45, null=False, primary_key=True)
    pw = models.CharField(max_length=45, null=False)
    category = models.CharField(max_length=45, null=False)
    name = models.CharField(max_length=45, null=False)
    phone = models.CharField(max_length=45, null=False)
    profile = models.FileField(upload_to="profile/")
    onoff = models.CharField(max_length=45, null=False, default='OFF')

    class Meta:
        db_table = 'counselor'
        managed = False


class calling(models.Model):
    c_no = models.AutoField(primary_key=True)
    cu_id = models.OneToOneField('customer',  on_delete=models.CASCADE, db_column='cu_id')
    co_id = models.ForeignKey('counselor',  on_delete=models.CASCADE, db_column='co_id')
    cu_name = models.CharField(max_length=45, null=False)
    co_name = models.CharField(max_length=45, null=False)
    current = models.CharField(max_length=45, null=False, default='대기')
    call_date = models.DateField(null=False)
    category = models.CharField(max_length=45, null=True)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'calling'
        managed = False


class point(models.Model):
    star_id = models.AutoField(primary_key=True)
    co_id = models.ForeignKey('counselor', on_delete=models.CASCADE, db_column='co_id')
    star = models.IntegerField(null=False)

    class Meta:
        db_table = 'point'
        managed = False
