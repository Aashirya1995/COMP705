from django.db import models

class Resume(models.Model):
    first_name = models.CharField(max_length=100,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=False,blank=False)

    def get_full_name(self): # function for the full_name
        return "{}, {}".format(self.first_name,self.last_name)

    def get_last_name_first_name(self): #function for the last name first;
        return "{}, {}".format(self.last_name,self.first_name)

    def get_experience(self): # function for experience
        return self.experience_set.all()

    def get_education(self): # function for education
        return self.education_set.all()

class Experience(models.Model):
    parent_resume = models.ForeignKey(Resume,on_delete=models.CASCADE,default = 1) # foreign key linking Experience to  Resume class.
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    parent_resume = models.ForeignKey(Resume,on_delete=models.CASCADE,default = 1) #foreign key linking Education to Resume class.
    instituition_name = models.CharField(max_length=100,null=False,blank=False)
    location = models.CharField(max_length=100,null=False,blank=False)
    degree = models.CharField(max_length=100,null=False,blank=False)
    major = models.CharField(max_length=100,null=False,blank=False)
    gpa = models.FloatField()

    def __str__(self):
        return self.instituition_name
