import datetime
import json
import uuid
from urllib.request import urlopen

from django.contrib import messages
from django.shortcuts import render, redirect

from web_pages.forms import WebPageForm
from web_pages.models import WebPage, WebRequest


def delete_old_web_obj():
    now = datetime.datetime.now()
    last = now - datetime.timedelta(days=5)
    WebPage.objects.filter(created_at__lte=last).delete()


# Create your views here.
def home(request):
    delete_old_web_obj()

    if request.session.get('uid') is None:
        request.session['uid'] = str(uuid.uuid4())[0:8]

    uid = request.session.get("uid")
    print(uid)

    pages = WebPage.objects.filter(browser_session=uid)

    context = {
        "pages": pages,
        'uid': uid,
    }

    return render(request, 'web_pages/home.html', context)


def create_web_page(request):
    if request.session.get('uid') is None:
        request.session['uid'] = str(uuid.uuid4())[0:8]

    uid = request.session.get("uid")
    path = request.get_host()
    form = WebPageForm()

    if request.method == 'POST':
        form = WebPageForm(request.POST)
        if form.is_valid():
            web_page = form.save(commit=False)
            web_page.browser_session = uid
            web_page.link = str(uuid.uuid4())[0:8]
            web_page.save()
            return redirect('home')

    context = {
        "form": form
    }
    return render(request, 'web_pages/create.html', context)


def save_request(request, uid):
    print(uid)
    try:
        page = WebPage.objects.get(link=uid)
        print(page)
        ip = request.META.get('REMOTE_ADDR')
        ip_location = get_location(ip)


        WebRequest.objects.create(
            web_page=page,
            header=request.META.get('HTTP_USER_AGENT'),
            ip=ip,
            country=ip_location['country'],
            city=ip_location['city'],
            isp=ip_location['isp'],
            region_name=ip_location['region_name']
        )

        return redirect(page.href_to)
    except Exception as e:
        print("error", e)

        return redirect('https://player.hu')


def get_location(ip):
    url = "http://ip-api.com/json/" + ip
    response = urlopen(url)
    data = json.loads(response.read())
    print(data)

    if data["status"] == "success":
        return {
            "country": data['country'],
            "city": data['city'],
            "isp": data['isp'],
            "region_name": data['regionName']
        }
    else:
        return {
            "country": "",
            "city": "",
            "isp": "",
            "region_name": ""
        }


def show_request(request, id):
    web_page = WebPage.objects.get(id=id)
    objs = web_page.web_requests.all()

    uid = request.session.get("uid")

    context = {
        "web_page": web_page,
        "objs": objs,
        'uid': uid,
    }

    return render(request, 'web_pages/requests.html', context)


def remove_web_page(request, pk):
    try:
        uid = request.session.get("uid")
        web_page = WebPage.objects.get(id=pk)

        if web_page.browser_session == uid:
            web_page.delete()
            print("success delete")
            messages.success(request, 'delete success')
        else:
            print("not permit")
            messages.warning(request, 'delete error')

    except Exception as e:
        print(e)
    return redirect('home')


def remove_request(request, pk):
    web_request = WebRequest.objects.get(pk=pk)
    id = web_request.web_page.pk
    try:
        uid = request.session.get("uid")

        if web_request.web_page.browser_session == uid:
            web_request.delete()
            print("success delete request")
            messages.success(request, 'delete success')
        else:
            print("not permit delete request")
            messages.warning(request, 'delete error')

    except Exception as e:
        print(e)
    return redirect('show_request',id)
