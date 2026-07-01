#removing white space from the right side of the string
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)


#removing white space from the left side and right side of the string
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
favorite_language = favorite_language.lstrip()
print(favorite_language)
print(' python')
print('python ')