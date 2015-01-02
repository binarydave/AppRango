from django.shortcuts import render
from apprango.models import Category, Page
from apprango.forms import CatForm, PageForm, UserForm, UserProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, resolve
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as dlogout
from django.contrib.auth import login as dlogin
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    # get and return the first 5 items in the Categories table
    all_categories = Category.objects.order_by("likes")[:5]
    return render(request, "apprango/index.html", {"objects": all_categories})


def category(request, slug_item):
    # a context item to be sent to the view
    context_item = {}

    try:
        # get the category with a matching slug
        category_ = Category.objects.get(slug=slug_item)
        context_item['name'] = category_.name

        # get all pages with a matching category
        pages = Page.objects.filter(category=category_)
        context_item['pages'] = pages

        context_item['category'] = category_

    except Category.DoesNotExist:
        # the requested category was not found
        # do nothing and go back
        # all necessary error messages are in the view
        pass

    return render(request, 'apprango/category.html', context_item)


@login_required
def add_category(request):
    if request.method == "POST":
        posted_form = CatForm(request.POST)

        if posted_form.is_valid():
            posted_form.save(commit=True)

            return HttpResponseRedirect(reverse("apprango:index"))
        else:
            messages.error(request, 'The category could not be created because of errors on the form.')
            return HttpResponseRedirect(reverse("apprango:add-category"))

    else:
        new_form = CatForm()
        return render(request, "apprango/add-category.html", {"form": new_form})


@login_required
def add_page(request, slug_item):
    try:
        catg = Category.objects.get(slug=slug_item)
    except Category.DoesNotExist:
        catg = None

    if request.method == 'POST':
        frm = PageForm(request.POST)

        if frm.is_valid():
            if catg:
                page = frm.save(commit=False)
                page.category = catg
                page.save()

                return HttpResponseRedirect(reverse('apprango:index'))
        else:
            # messages.error(request, 'The page could not be added because of errors on the form.')
            # return HttpResponseRedirect(reverse('apprango:add-page', args=(catg.slug, ), kwargs={'form': frm}))
            context_dict = {'form': frm, 'category': catg}
            return render(request, 'apprango/add-page.html', context_dict)
    else:
        frm = PageForm()
        context_dict = {'form': frm, 'category': catg}
        return render(request, 'apprango/add-page.html', context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        form_user = UserForm(data=request.POST)
        form_profile = UserProfileForm(data=request.POST)

        if form_profile.is_valid() and form_user.is_valid():
            usr = form_user.save(commit=False)
            usr.set_password(usr.password)
            usr.save()

            prfl = form_profile.save(commit=False)
            prfl.user = usr

            if 'picture' in request.FILES:
                prfl.picture = request.FILES['picture']

            prfl.save()
            registered = True
            context_dict = {'frm_user': form_user, 'frm_profile': form_profile, 'registered': registered}
            return render(request, 'apprango/register.html', context_dict)

        else:
            context_dict = {'frm_user': form_user, 'frm_profile': form_profile}
            return render(request, 'apprango/register.html', context_dict)

    else:
        form_user = UserForm()
        form_profile = UserProfileForm()
        context_dict = {'frm_user': form_user, 'frm_profile': form_profile, 'registered': registered}
        return render(request, 'apprango/register.html', context_dict)


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['passw']

        usr = authenticate(username=uname, password=passw)

        if usr and usr.is_active:
            dlogin(request, usr)
            next_pg = request.POST['next']

            if next_pg:
                pg_match = resolve(next_pg)
                return HttpResponseRedirect(reverse(pg_match.view_name, kwargs=pg_match.kwargs))
            else:
                return HttpResponseRedirect(reverse('apprango:index'))
        else:
            messages.error(request, 'Your login credentials are invalid')
            return HttpResponseRedirect(reverse('apprango;login.html'))

    else:
        next_pg = request.GET.get('next', False)
        if next_pg:
            return render(request, 'apprango/login.html', {'next': next_pg})
        else:
            return render(request, 'apprango/login.html')


@login_required
def restricted(request):
    return HttpResponse('Hello. It appears you are logged in :)')


@login_required
def logout(request):
    dlogout(request)
    return HttpResponseRedirect(reverse('apprango:index'))