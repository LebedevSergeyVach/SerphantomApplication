from django.shortcuts import render


class WebViews(object):
    """Web views for the app."""

    def welcome(request):
        return render(
            request, 'welcome.html'
        )

    def index_windows(request):
        return render(
            request, 'application_windows/index.html'
        )

    def index_android(request):
        return render(
            request, 'application_android/index.html'
        )

    def add_windows_post(request):
        return render(
            request, 'application_windows/add-windows-post.html'
        )

    def add_android_post(request):
        return render(
            request, 'application_android/add-android-post.html'
        )

    def not_found(request):
        return render(
            request, '404.html'
        )
