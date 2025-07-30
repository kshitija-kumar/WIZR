from django.shortcuts import render, get_object_or_404
from .models import Meeting

def meetings_list(request):
    meetings = Meeting.objects.all()
    return render(request, "fund_manager_conversations/meetings_list.html", {"meetings": meetings})

def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    return render(request, "fund_manager_conversations/meeting_detail.html", {"meeting": meeting})
