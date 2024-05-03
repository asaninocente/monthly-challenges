from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Challenge for April',
    'may': 'Challenge for May',
    'june': 'Challenge for June',
    'july': 'Challenge for July',
    'august': 'Challenge for August',
    'september': 'Challenge for September',
    'october': 'Challenge for October',
    'november': 'Challenge for November',
    'december': None
}

# Create your views here.

def index(request):
    # list_items = ''
    months = list(monthly_challenges.keys())
    
    # for month in months:
        # capitalized_month = month.capitalize()
        # month_path = reverse('month-challenge', args=[month])
        # list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
        
    # response_data = f'<ul>{list_items}</ul>'
    # return HttpResponse(response_data)
    return render(request, 'challenges/index.html', {
        'months': months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month</h1>')
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month_name': month
        }) #f'<h1>{challenge_text}</h1>'
    except:
        #response_data = render_to_string('404.html')
        raise Http404()
        #return HttpResponseNotFound(response_data)