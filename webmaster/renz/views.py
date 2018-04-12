from django.shortcuts import render
import re
import os

def clean(raw):
    cleanr = re.compile('<.*?>')
    clean2 = re.compile('<style>.*</style>',  flags=re.DOTALL)
    clean3 = re.compile('<script>.*</script>',  flags=re.DOTALL)
    cleantext = re.sub(clean2, '', raw)
    cleantext = re.sub(clean3, '', raw)
    cleantext = re.sub(cleanr, '', raw)
    return cleantext

def search(request):
    module_dir = os.path.dirname(__file__)+'//templates//renz'  # get current directory
    searched = request.GET.get('search')
    a = open(os.path.join(module_dir, 'indexgang.html'), 'r')
    b = open(os.path.join(module_dir, 'about.html'), 'r')
    c = open(os.path.join(module_dir, 'products.html'), 'r')
    d = open(os.path.join(module_dir, 'contact.html'), 'r')

    aa = a.read()
    bb=b.read()
    cc=c.read()
    dd=d.read()
    A = clean(aa)
    B= clean(bb)
    C= clean(cc)
    D= clean(dd)

    pattern = re.compile(searched, re.I)

    p1=pattern.search(A)
    p2=pattern.search(B)
    p3=pattern.search(C)
    p4=pattern.search(D)

    P1=None
    P2=None
    P3=None
    P4=None

    if p1:
        P1 = 'HOME'

    if p2:
        P2 = 'ABOUT US'

    if p3:
        P3 = 'PRODUCTS'

    if p4:
        P4 = 'CONTACT'

    Ps = [P1, P2, P3, P4]

    PS=0

    for i in Ps:
        if i!=None:
            PS+=1


    message = P1
    message2 = P2
    message3 = P3
    message4 = P4

    template = "renz/search.html"
    context = {
        'message': message,
        'message2': message2,
        'message3': message3,
        'message4': message4,
        'PS': PS,
    }
    return render(request, template, context)

def home(request):
    template = "renz/indexgang.html"
    context = {}
    return render(request, template, context)

def about(request):
    template = "renz/about.html"
    context = {}
    return render(request, template, context)

def products(request):
    template = "renz/products.html"
    context = {}
    return render(request, template, context)

def contact(request):
    template = "renz/contact.html"
    context = {}
    return render(request, template, context)
def school(request):
    template = "renz/School Website.html"
    context = {}
    return render(request, template, context)
def image(request):
    template = "renz/Images Page.html"
    context = {}
    return render(request, template, context)
def course(request):
    template = "renz/Course Summaries.html"
    context = {}
    return render(request, template, context)
def teach(request):
    template = "renz/School Teachers.html"
    context = {}
    return render(request, template, context)

def buy(request):

    query = request.GET.get('quantity1')
    query2 = request.GET.get('quantity2')
    query3 = request.GET.get('quantity3')

    queries = [query, query2, query3]


    for i in range(len(queries)):
        if queries[i] == '' or queries[i] == None:
            queries[i]='0'

    message = "You owe ${}".format(int(queries[0]) * 12000 +
                                            int(queries[1]) * 70000 +
                                            int(queries[2]) * 20000)
    message2 = "Buying {} ALPHA(s), {} A-TURING(s), {} A-HOME(s)".format(
            queries[0], queries[1], queries[2])


    template = "renz/buy.html"
    context = {
        'message': message,
        'message2': message2,
        'queries':queries,
    }
    return render(request, template, context)
