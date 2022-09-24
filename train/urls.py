"""URL patterns for Personal Training App"""
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("contact",views.contact,name="contact"),
    path("index", views.index, name="index"),
        path("events",views.events,name="event"),
        path("<int:pnum>", views.index, name="index"),
        path("login", views.login_view, name="login"),
        path("logout", views.logout_view, name="logout"),
        path("register", views.register, name="register"),
        path("newsession", views.newsession, name="newsession"),
        path("newsession/<int:pk>", views.sessionview, name="sessionview"),
        path("editsession", views.editsession, name="editsession"),
        path("editsession/<int:session>", views.editsession, name="editsession"),
        path("routines/new", views.newroutine, name="newroutine"),
        path("routines/edit", views.routinelist, name="routinelist"),
        path("routines/edit/<int:pk>", views.editroutine, name="editroutine"),
        path("exercises", views.exerciseview, name="exerciseview"),
        path("charts", views.charts, name="charts"),
        path("charts/<int:pnum>", views.charts, name="charts"),

        path("clientroutines", views.clientroutines, name="clientroutines"),
        path("clientroutines/<int:pnum>", views.clientroutines, name="clientroutines"),
        path("clientprogress", views.clientprogress, name="clientprogress"),

        path("postset", views.postset, name="postset"),
        path("setgroupinfo", views.setgroupinfo, name="setgroupinfo"),
        path("deletex", views.deletex, name="deletex"),
        path("deletesession/<int:sessionpk>", views.deletesession, name="deletesession"),
        path("checkcomplete/<int:sessionpk>", views.checkcomplete, name="checkcomplete"),
        path("deleteempties/<int:sessionpk>", views.deleteempties, name="deleteempties"),
        path("fetchsessions/<int:client>", views.fetchsessions, name="fetchsessions"),
        path("updateset", views.updateset, name="updateset"),
        path("archive/<int:routine>", views.archive, name="archive"),
        path("anotherexercise", views.anotherexercise, name="anotherexercise"),
        path("progressAPI/<int:exercise>", views.progressAPI, name="progressAPI")
]
