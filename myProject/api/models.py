from django.db import models

# Define the Car model
class Car(models.Model):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('white', 'White'),
        ('silver', 'Silver'),
    ]

    registration_number = models.CharField(max_length=20, unique=True)
    owner_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    make_year = models.IntegerField()
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)

    def __str__(self):
        return f"{self.registration_number} - {self.model_name}"


# Define the WheelForm models
class WheelForm(models.Model):
    form_number = models.CharField(max_length=100, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()

    def __str__(self):
        return self.form_number


class WheelField(models.Model):
    form = models.OneToOneField(WheelForm, related_name='fields', on_delete=models.CASCADE)

    treadDiameterNew = models.CharField(max_length=50)
    lastShopIssueSize = models.CharField(max_length=50)
    condemningDia = models.CharField(max_length=50)
    wheelGauge = models.CharField(max_length=50)
    variationSameAxle = models.CharField(max_length=50)
    variationSameBogie = models.CharField(max_length=50)
    variationSameCoach = models.CharField(max_length=50)
    wheelProfile = models.CharField(max_length=100)
    intermediateWWP = models.CharField(max_length=50)
    bearingSeatDiameter = models.CharField(max_length=100)
    rollerBearingOuterDia = models.CharField(max_length=100)
    rollerBearingBoreDia = models.CharField(max_length=100)
    rollerBearingWidth = models.CharField(max_length=100)
    axleBoxHousingBoreDia = models.CharField(max_length=100)
    wheelDiscWidth = models.CharField(max_length=100)

CONDITION_CHOICES = [
    ('good', 'Good'),
    ('fair', 'Fair'),
    ('poor', 'Poor'),
    ('bad', 'Bad'), 
    ]

# Define the bogie-related models

class bogieForm(models.Model):
    form_number = models.CharField(max_length=100, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()

    def __str__(self):
        return self.form_number

class bogieDetailsForm(models.Model):
    form = models.OneToOneField(bogieForm, related_name='bogieDetails', on_delete=models.CASCADE)

    bogieNo = models.CharField(max_length=50)
    makerYearBuilt = models.CharField(max_length=50)
    incomingDivAndDate = models.CharField(max_length=100)
    deficitComponents = models.CharField(max_length=100)
    dateOfIOH = models.DateField()

class bogieChecksheetForm(models.Model):
    form = models.OneToOneField(bogieForm, related_name='bogieChecksheet', on_delete=models.CASCADE)

    bogieFrameCondition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    bolster = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    bolsterSuspensionBracket = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    lowerSpringSeat = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    axleGuide = models.CharField(max_length=50, choices=CONDITION_CHOICES)

class bmbcChecksheetForm(models.Model):
    form = models.OneToOneField(bogieForm, related_name='bmbcChecksheet', on_delete=models.CASCADE)

    cylinderBody = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    pistonTrunnion = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    adjustingTube = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    plungerSpring = models.CharField(max_length=50, choices=CONDITION_CHOICES)