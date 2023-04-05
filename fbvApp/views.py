from django.shortcuts import render , redirect
from fbvApp.models import Student
from fbvApp.models import Login
from fbvApp.forms import StudentForm
from fbvApp.forms import LoginForm
from fbvApp.models import Todo
from fbvApp.forms import TodoForm

#-----------------------------------------------------------------------------

# for the Login 
username = ''
def login(request):
    global username
    login = LoginForm()
    message=''
    if request.method=='POST':
        login = LoginForm(request.POST)
        if login.is_valid():
            print(request.POST['username'] , request.POST['password'])
            username = request.POST['username']
            password = request.POST['password']
            logins = Login.objects.all()                         #Now checking this user and pass , matched with our record in Database
            for l in logins:
                if l.username==username and l.password==password:
                    return redirect('/home')                     #Give access to the website
                        
                else:
                    message = "Invalid Username/Password"        #If wrong credentials , just show back the login form page
        
    #if request is get type get return the same login page with login form and a message    
    return render(request , 'fbvApp/login.html' , {'login' : login , 'message':message })

#-----------------------------------------------------------------------------

# for Home page : Todo Task addition  
def getStudent(request):
    todos = Todo.objects.all()                 #Fetching list of Todo from Db
    todoForm = TodoForm()                      #Creating form for adding todo
    if request.method=='POST':

        todoForm = TodoForm(request.POST)
        if todoForm.is_valid():
            print('todo form is valid')
            print(todoForm.cleaned_data)
            todoForm.save()
            return redirect('/home')
                                               #Just displaying the list of todos
    li = []
    for l in todos:
        print(l.username , l.title , l.description)
        if l.username==username:
            li.append(l)
            print('inside if')
    return render(request , 'fbvApp/index.html' , {'todos':li , 'todoForm': todoForm , 'username' : username})





#-----------------------------------------------------------------------------

def deleteStudent(request , id):
    print('Id We Got as ' , id)
    student = Todo.objects.get(id = id)
    print(student)
    student.delete()
    return redirect('/home')


#-----------------------------------------------------------------------------


def updateStudent(request , id):
    todo = Todo.objects.get(id = id)
    todoForm = TodoForm(instance=todo)
    if request.method=='POST':
        todoForm = TodoForm(request.POST , instance=todo)
        if todoForm.is_valid():
           todoForm.save()
           print(todoForm.cleaned_data)
           return redirect("/home")
    
    return render(request , 'fbvApp/update.html'  , {'todoForm' : todoForm})



#-----------------------------------------------------------------------------

# End point for   registering the new User
def register(request):
    login = LoginForm()
    if request.method=='POST':
         form = LoginForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('/' , {'message' : 'User Registered Successfully'})
    
    return render(request , 'fbvApp/register.html' , {'login' : login})



#-----------------------------------------------------------------------------






































#-----------------------------------------------------------------------------

def createStudent(request):
    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request , 'fbvApp/create.html' , {'form' : form})
