import face_recognition

image = face_recognition.load_image_file('./img/groups/cr y lm.jpg')
face_locations = face_recognition.face_locations(image)

# Array of coords
print(face_locations)

# Number of people
print(f'The number of people is {len(face_locations)}')  # f to use a variable
