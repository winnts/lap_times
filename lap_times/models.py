from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.surname, self.name)


class CarMake(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarSubModel(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarEngineDisplacement(models.Model):
    displacement = models.CharField(max_length=50)

    def __str__(self):
        return self.displacement


class CarDrivetrain(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class Car(models.Model):
    name = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, null=True, blank=True, on_delete=models.CASCADE)
    sub_model = models.ForeignKey(CarSubModel, null=True, blank=True, default='-', on_delete=models.CASCADE)
    displacement = models.ForeignKey(CarEngineDisplacement, null=True, blank=True, on_delete=models.CASCADE)
    drivetrain = models.ForeignKey(CarDrivetrain, null=True, blank=True, on_delete=models.CASCADE)
    weight = models.CharField(max_length=10, null=True, blank=True, default='-',)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.name, self.model, self.sub_model, self.displacement, self.drivetrain,
                                          self.weight)


class TyreMake(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TyreModel(models.Model):
    make = models.ForeignKey(TyreMake, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.model


class TyreRadius(models.Model):
    radius = models.IntegerField()

    def __str__(self):
        return str(self.radius)


class TyreHeight(models.Model):
    height = models.IntegerField()

    def __str__(self):
        return str(self.height)


class TyreWidth(models.Model):
    width = models.IntegerField()

    def __str__(self):
        return str(self.width)


class TyreTreadwear(models.Model):
    treadwear = models.IntegerField()

    def __str__(self):
        return str(self.treadwear)


class Tyre(models.Model):
    make = models.ForeignKey(TyreMake, on_delete=models.CASCADE)
    model = models.ForeignKey(TyreModel, on_delete=models.CASCADE)
    width = models.ForeignKey(TyreWidth, on_delete=models.CASCADE)
    height = models.ForeignKey(TyreHeight, on_delete=models.CASCADE)
    radius = models.ForeignKey(TyreRadius, on_delete=models.CASCADE)
    treadwear = models.ForeignKey(TyreTreadwear, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.make) + ' ' + \
               str(self.model) + ' ' + \
               str(self.width) + '/' + \
               str(self.height) + 'R' + \
               str(self.radius) + ' TW' + \
               str(self.treadwear)


class Track(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EventName(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    track = models.ForeignKey(Track, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} | Track: {}".format(self.name, self.date, self.track)


class EventClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TrackTime(models.Model):
    name = models.ForeignKey(EventName, verbose_name='Event name', on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    event_class = models.ForeignKey(EventClass, null=True, blank=True, on_delete=models.CASCADE)
    tyre = models.ForeignKey(Tyre, null=True, blank=True, on_delete=models.CASCADE)
    best_time = models.DurationField()

    # @property
    # def best_time(self):
    #     return "{}".format(self.best_time)

    def __str__(self):
        return "{} | {} | {} | Tyres: {} | Best time: {}".format(self.name, self.driver, self.car, self.tyre,
                                                                 self.best_time)
