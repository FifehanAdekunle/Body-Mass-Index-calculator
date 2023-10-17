#!/usr/bin/env python
# coding: utf-8

# In[1]:


# input
name = input ("Enter your name")
weight = int (input('Enter your weight in pounds:'))
Height = int (input('Enter your height in inches:'))
BMI = (weight * 703)/ (Height* Height)
print(int (BMI))


# In[3]:


#if elif and else satement
if BMI > 0:
    if (BMI< 18.5):
        print (name + " , You are under weight.")
    elif (BMI<= 29.9):
        print (name + ", You are normal weight.")
    elif (BMI < 29.9 ):
        print (name + ", You are overweight. You need to exercise more")
    elif (BMI< 34.9):
        print (name + ", You are obese.You need to exercise more")
    elif (BMI ):
        print (name + ", You are severly obese.You need to exercise more")
        
    else: 
        print (name +', You are mordily obese You need to exercise more')
else: 
    print ('Enter Valid Input')


# In[ ]:


# input & if elif and else satement combined to form calculator
name = input ("Enter your name")
weight = int (input('Enter your weight in pounds:'))
Height = int (input('Enter your height in inches:'))
BMI = (weight * 703)/ (Height* Height)
print(int (BMI))

if BMI > 0:
    if (BMI< 18.5):
        print (name + " , You are under weight.")
    elif (BMI<= 29.9):
        print (name + ", You are normal weight.")
    elif (BMI < 29.9 ):
        print (name + ", You are overweight. You need to exercise more")
    elif (BMI< 34.9):
        print (name + ", You are obese.You need to exercise more")
    elif (BMI ):
        print (name + ", You are severly obese.You need to exercise more")
        
    else: 
        print (name +', You are mordily obese You need to exercise more')
else: 
    print ('Enter Valid Input')


# In[1]:


#code from Chat gpt to design the calculator
import ipywidgets as widgets
from IPython.display import display

# Create input fields
name_input = widgets.Text(placeholder="Enter your name", description="Name:", style={'description_width': 'initial'})
weight_input = widgets.FloatSlider(value=150, min=0, max=500, step=1, description="Weight (lbs):", style={'description_width': 'initial'})
height_input = widgets.FloatSlider(value=60, min=0, max=100, step=1, description="Height (inches):", style={'description_width': 'initial'})

# Create a button to calculate BMI
calculate_button = widgets.Button(description="Calculate BMI", button_style='info')

# Output widget to display the result
output = widgets.Output()

# BMI calculation function
def calculate_bmi(b):
    weight = weight_input.value
    height = height_input.value
    BMI = (weight * 703) / (height * height)
    
    with output:
        output.clear_output()
        if BMI > 0:
            if BMI < 18.5:
                print(name_input.value + ", You are underweight.")
            elif BMI <= 24.9:
                print(name_input.value + ", You are a normal weight.")
            elif BMI <= 29.9:
                print(name_input.value + ", You are overweight. You need to exercise more.")
            elif BMI <= 34.9:
                print(name_input.value + ", You are obese. You need to exercise more.")
            else:
                print(name_input.value + ", You are severely obese. You need to exercise more.")
        else:
            print('Enter valid input')

calculate_button.on_click(calculate_bmi)

# Display widgets
display(name_input, weight_input, height_input, calculate_button, output)


# In[ ]:




