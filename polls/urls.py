from django.urls import include, path
from polls.views import polls_index_view, polls_show_view,vote, results,add_question_page

app_name = 'polls'
urlpatterns = [
    path('', polls_index_view, name="polls-index"),
    path('add/', add_question_page, name="polls-add"),
    path('<int:question_id>', polls_show_view, name="polls-detail"),
    path('<int:question_id>/results/', results, name="polls-result"),
    path('<int:question_id>/vote/', vote, name="polls-vote"),

]
