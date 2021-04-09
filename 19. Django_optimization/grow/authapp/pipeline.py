from social_core.exceptions import AuthForbidden

from authapp.models import GrowUserProfile


def save_profile(backend, user, response, *args, **kwargs):
    print(response['picture'])
    if backend.name == "google-oauth2":
        if 'gender' in response.keys():
            if response['gender'] == 'male':
                user.growuserprofile.gender = GrowUserProfile.MALE
            else:
                user.growuserprofile.gender = GrowUserProfile.FEMALE

        if 'scope' in response.keys():
            user.growuserprofile.url_user = response['scope']

        if 'locale' in response.keys():
            user.growuserprofile.language_user = response['locale']

        if 'picture' in response.keys():
            url = response['picture']
            user.avatar_user = url

        if 'ageRange' in response.keys():
            minAge = response['ageRange']['min']
            if int(minAge) < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.google.GoogleOAuth2')
            else:
                user.growuserprofile.user_age = response['ageRange']['min']
        user.save()
        # user.growuserprofile.save()