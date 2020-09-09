from django.views.generic import TemplateView


#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

class RoomView(TemplateView):
    template_name = 'room.html'

class login(TemplateView):
    template_name = 'log.html'

class room_info(TemplateView):
    template_name = 'room_info.html'
