from django.urls import path
from .views import (
    HomeView,
    MailingListView,
    MailingDetailView,
    MailingCreateView,
    MailingUpdateView,
    MailingDeleteView,
    RecipientListView,
    RecipientCreateView,
    RecipientUpdateView,
    RecipientDeleteView,
    MessageListView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    AttemptListView
)

urlpatterns = [

    # =====================
    # Главная
    # =====================
    path('', HomeView.as_view(), name='home'),

    # =====================
    # MAILINGS
    # =====================
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    # =====================
    # RECIPIENTS
    # =====================
    path('recipients/', RecipientListView.as_view(), name='recipient_list'),
    path('recipients/create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipients/<int:pk>/update/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipients/<int:pk>/delete/', RecipientDeleteView.as_view(), name='recipient_delete'),

    # =====================
    # MESSAGES
    # =====================
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path(
    "attempts/",
    AttemptListView.as_view(),
    name="attempt_list",
),
]