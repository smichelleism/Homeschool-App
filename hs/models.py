from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

class HomeschoolApplication(models.Model):

	LEVEL24	= '24'
	LEVEL35	= '35'
	LEVEL65 = '65'
	LEVEL99 = '99'

	HH_INCOME_CHOICES	= (
		(LEVEL24, "Below 24,000"),
		(LEVEL35, "Between 24,000 and 35,000"),
		(LEVEL65, "Between 35,000 and 65,000"),
		(LEVEL99, "Above 65,000"),
		)

	IR = 'IR'
	HS = 'HS'
	GC = 'GC'
	FS = 'FS'
	
	RESCUE_CHOICES = (
		(IR, "Indie Rescuer"),
		(HS, "Homeschool"),
		(GC,"Guidence Counselor"),
		(FS, "Foster"))

	CLOSED 		= 'C'
	OPEN		= 'O'
	ACTIVE 		= 'A'
	PENDING		= 'P'
	NEWCONTACT 	= 'N'

	APPLICATION_STATUS_CHOICES = (
		(ACTIVE, "Active"),
		(OPEN, "Open"),
		(CLOSED, "Closed"),
		(PENDING, "Pending"),
		(NEWCONTACT, "New Contact"))

	application_status 	= models.CharField(max_length = 1, choices = APPLICATION_STATUS_CHOICES, default = NEWCONTACT)
	rescue_type			= models.CharField(max_length = 2, choices = RESCUE_CHOICES, blank=True, null=True)
	hh_income	 		= models.CharField(max_length = 2, choices=HH_INCOME_CHOICES, verbose_name="What is your household income?", blank=True, null=True)
	application_date	= models.DateTimeField(default=timezone.now)
	first_name          = models.CharField(verbose_name='What is your first name?', max_length=100)
	last_name           = models.CharField(verbose_name='What is your family (last) name?',  max_length=100)
	email               = models.CharField(verbose_name='What is your email?',  max_length=100)
	street_address  	= models.CharField(verbose_name='What is your street address?',  max_length=200, blank=True, null=True)
	city            	= models.CharField(verbose_name='What is your city?', max_length=50,  blank=True, null=True)
	state           	= models.CharField(verbose_name='What state do you live in?',max_length=2, default="CA", blank=True, null=True)
	zipcode         	= models.CharField(verbose_name='What is your zip code?', max_length=10, blank=True, null=True)
	phone_cell			= models.CharField(verbose_name='What is your cell phone number?',max_length=20, blank=True, null=True)
	phone_land			= models.CharField(verbose_name='What is your home telephone number?', max_length=20, blank=True, null=True)
	occupation			= models.CharField(verbose_name="What is your occupation?",max_length=50,blank=True, null=True)
	own_cats			= models.CharField(verbose_name="Do you own cats?",max_length=50,blank=True, null=True)
	other_pets			= models.CharField(verbose_name="Do you have any other pets?",max_length=50,blank=True, null=True)
	date_found			= models.DateField(verbose_name="When did you find the kitten(s)?",blank=True, null=True)
	num_found			= models.CharField(verbose_name="How many kitten(s) were found?",max_length=50,blank=True, null=True)
	location	        = models.CharField(verbose_name='Where you find the kitten(s). Was it a business/home/school/field/or ...',  max_length=100,  blank=True, null=True)
	seen_mom			= models.CharField(verbose_name="Have you seen the mom-cat?",max_length=50,blank=True, null=True)
	seen_other_strays	= models.CharField(verbose_name="Have you seen other strays?",max_length=50,blank=True, null=True)
	notes_public        = models.TextField(verbose_name='Is there any additional information which would helpful?', blank=True, null=True)
	notes_private       = models.TextField(verbose_name='Private KB Notes.', blank=True, null=True)


	def __str__(self):
		return self.last_name + ', ' + self.first_name



class Kitten (models.Model):

	ADOPTED		= 'A'
	RELEASED	= 'R'
	DECEASED 	= 'D'
	INTAKE 		= 'I'
	FOSTERFAIL 	= 'F'
	ESCAPED		= 'E'
	TIAA		= 'T'
	OTHER 		= 'O'

	OUTCOME_CHOICES	= (
		(ADOPTED, "Adopted"),
		(DECEASED, "Deceased"),
		(ESCAPED, "Escaped"),
		(FOSTERFAIL, "Foster Fail Adoption"),
		(INTAKE, "Intake"),
		(RELEASED, "Released"),
		(TIAA, "TIAA"),
		(OTHER, "Other")
		)

	outcome	 					= models.CharField(max_length = 1, choices=OUTCOME_CHOICES, blank=True, null=True)
	name 						= models.CharField(max_length=50, blank=True, null=True)
	description 				= models.CharField(max_length=100,blank=True, null=True)
	birthdate 					= models.DateField(blank=True, null=True)
	first_assessment 			= models.DateField(blank=True, null=True)
	first_assessment_weight 	= models.CharField(max_length=20,blank=True, null=True)
	second_assessment 			= models.DateField(blank=True, null=True)
	second_assessment_weight	= models.CharField(max_length=20,blank=True, null=True)
	FVRCP_01 					= models.DateField(blank=True, null=True)
	FVRCP_01_note 				= models.CharField(max_length=20,blank=True, null=True)
	FVRCP_02 					= models.DateField(blank=True, null=True)
	FVRCP_02_note 				= models.CharField(max_length=20,blank=True, null=True)
	deworm_01 					= models.DateField(blank=True, null=True)
	deworm_01_note 				= models.CharField(max_length=20,blank=True, null=True)
	deworm_02 					= models.DateField(blank=True, null=True)
	deworm_02_note 				= models.CharField(max_length=20,blank=True, null=True)
	flea_01 					= models.DateField(blank=True, null=True)
	flea_01_note 				= models.CharField(max_length=20,blank=True, null=True)
	flea_02 					= models.DateField(blank=True, null=True)
	flea_02_note 				= models.CharField(max_length=20,blank=True, null=True)
	sneuter 					= models.DateField(blank=True, null=True)
	sneuter_location 			= models.CharField(max_length=50,blank=True, null=True)
	notes 						= models.TextField(blank=True, null=True)
	application 				= models.ForeignKey(HomeschoolApplication, blank=True, null=True) 


	def return_age():
		delta = datetime.timedelta(datetime.now - birthdate)
		return delta/7


