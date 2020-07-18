from django.db import models
from django.core.validators import RegexValidator

SEX_TYPE = (
    ('male', 'male'),
    ('female', 'female')
)

FEE_TYPE = (
    ('three', '3'),
    ('six', '6'),
    ('twelve', '12')
)


class Client(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=12, null=True, blank=True)
    user_id = models.ImageField(upload_to="staff/", null=True, blank=True, default='')
    pic = models.ImageField(upload_to='client/', null=True, blank=False)
    join_date = models.DateField(null=False, blank=False)


class Staff(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=12, null=True, blank=True)
    user_id = models.ImageField(upload_to="staff/", null=True, blank=True, default='')
    pic = models.ImageField(upload_to='staff/', null=True, blank=False)
    join_date = models.DateField(null=False, blank=False)


class Visitor(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=12, null=True, blank=True)


class Blog(models.Model):
    heading = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(max_length=500, null=False, blank=False)
    pic = models.ImageField(upload_to='blog/', null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            url = self.pic.url
        except:
            url = ''
        return url


class Contact_us(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=False)
    comment = models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.name


class Calculate_BMI(models.Model):
    height = models.FloatField(max_length=10, null=False)
    weight = models.FloatField(max_length=10, null=False)
    age = models.FloatField(max_length=10, null=False)
    sex = models.CharField(max_length=100, choices=SEX_TYPE, default='male')


class Trainer(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    qualification = models.TextField(max_length=200, null=False, blank=False)
    trainer_id = models.ImageField(upload_to="trainer/", null=True, blank=True, default='')
    facebook = models.CharField(max_length=500, null=True, blank=True, default='')
    instagram = models.CharField(max_length=500, null=True, blank=True, default='')
    tweet = models.CharField(max_length=500, null=True, blank=True, default='')
    picture = models.ImageField(upload_to='trainer/', null=True, blank=True, default='')

    def __str__(self):
        return self.name

    @property
    def trainer_imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


class Achivement(models.Model):
    a_image = models.ImageField(upload_to='achivement/', null=False, blank=False)
    about_image = models.TextField(max_length=200, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.a_image.url
        except:
            url = ''
        return url


class Equipment(models.Model):
    e_image = models.ImageField(upload_to='equipment/', null=False, blank=False)

    @property
    def imageURL(self):
        try:
            url = self.e_image.url
        except:
            url = ''
        return url


class Price(models.Model):
    month = models.CharField(max_length=200, choices=FEE_TYPE, default='six')
    price = models.IntegerField(null=False, blank=False)


class Home_pic_moti(models.Model):
    h_image = models.ImageField(upload_to='home/', null=False, blank=False)
    motivation = models.CharField(max_length=300, null=False, blank=False)

    @property
    def imageURL(self):
        try:
            url = self.h_image.url
        except:
            url = ''
        return url


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/", null=False, blank=False)
    text = models.TextField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    star = models.IntegerField(null=False, blank=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def get_text1(self):
        n = len(self.text)
        if n > 100:
            return self.text[:100]
        else:
            return self.text[:n]

    @property
    def get_text2(self):
        return self.text[100:]


class Info(models.Model):
    address = models.CharField(max_length=200, null=False, blank=False)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
