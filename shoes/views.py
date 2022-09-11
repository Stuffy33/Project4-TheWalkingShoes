from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import ShoePair
from .forms import SubmitShoesForm


class ShoessPage(generic.ListView):
    #View ShoessPage
    model = ShoePair
    queryset = ShoePair.objects.filter(status=1).order_by('-created_on')
    template_name = 'shoess.html'
    paginate_by = 12

def submit_shoes(request):
    #View for shoes submission page
    if request.method == 'POST':
        submission_form = SubmitShoesForm(request.POST, request.FILES)
        if submission_form.is_valid():
            submission_form.instance.trader = request.user
            submission_form.save()
            messages.success(
                request, "Submission has been successfull. Your trade will show up on our page as soon as it has been reviewed")
            return redirect('shoess')
        else:
            submission_form = SubmitShoesForm()

    return render(
        request,
        'submit-shoes.html',
        {
            'submission_form': SubmitShoesForm(),
        },
    )

def edit_shoes(request, slug):
    #Edit submitted trade
    shoess = get_object_or_404(ShoePair, slug=slug)
    edit_form = SubmitShoesForm(request.POST or None, instance=shoess)
    context = {
        'edit_form': edit_form,
        'shoess': shoess
    }

    if request.method == 'POST':
        edit_form = SubmitShoesForm(
            request.POST, request.FILES, instance=shoess)
        if edit_form.is_valid():
            shoess = edit_form.save(commit=False)
            shoess.trader = request.user
            shoess.save()
            return redirect('shoess')
    else:
        edit_form = SubmitShoesForm(instance=shoess)

    return render(request, 'edit-shoes.html', context)

def delete_shoes(request, slug):
    #Delete submitted shoes
    shoess = get_object_or_404(ShoePair, slug=slug)
    shoess.delete()
    return redirect('shoess')


class ShoesDetails(View):
    # Render shoes to site
    def get(self, request, slug, *args, **kwargs):
        #Obtain print & check for likes.
        queryset = ShoePair.objects.filter(status=1)
        shoess = get_object_or_404(queryset, slug=slug)
        liked = False
        if shoess.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'shoes-details.html',
            {
                'shoess': shoess,
                'liked': liked,
            }
        )

# Class used from "I think therefore I blog" walkthrough.
class LikeShoePair(View):
    #let users like shoe submitions
    def post(self, request, slug):
        #Check if user likes posts
        shoess = get_object_or_404(ShoePair, slug=slug)
        if shoess.likes.filter(id=request.user.id).exists():
            shoess.likes.remove(request.user)
        else:
            shoess.likes.add(request.user)
        return HttpResponseRedirect(reverse('shoes_detail', args=[slug]))
