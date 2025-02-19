import unittest
import json
from Smart_Home_Api import app  # Import the Flask app from your main file

class SmartHomeApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_create_user(self):
        response = self.app.post('/users', json={"username": "JohnDoe", "house_id": 1})
        self.assertEqual(response.status_code, 201)
        self.assertIn("User created successfully", response.get_data(as_text=True))
    
    def test_create_user_missing_fields(self):
        response = self.app.post('/users', json={})
        self.assertEqual(response.status_code, 400)
    
    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
    
    def test_update_user(self):
        response = self.app.put('/users/1', json={"username": "JohnUpdated", "house_id": 1})
        self.assertEqual(response.status_code, 200)
        self.assertIn("User updated successfully", response.get_data(as_text=True))
    
    def test_delete_user(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("User deleted successfully", response.get_data(as_text=True))
    
    def test_create_house(self):
        response = self.app.post('/houses', json={"username": "JohnDoe", "num_rooms": 4})
        self.assertEqual(response.status_code, 201)
        self.assertIn("House created successfully", response.get_data(as_text=True))
    
    def test_get_houses(self):
        response = self.app.get('/houses')
        self.assertEqual(response.status_code, 200)
    
    def test_update_house(self):
        response = self.app.put('/houses/1', json={"username": "JohnDoe", "num_rooms": 5})
        self.assertEqual(response.status_code, 200)
        self.assertIn("House updated successfully", response.get_data(as_text=True))
    
    def test_delete_house(self):
        response = self.app.delete('/houses/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("House deleted successfully", response.get_data(as_text=True))
    
    def test_create_room(self):
        response = self.app.post('/rooms', json={"username": "JohnDoe", "room_name": "Living Room"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Room created successfully", response.get_data(as_text=True))
    
    def test_get_rooms(self):
        response = self.app.get('/rooms')
        self.assertEqual(response.status_code, 200)
    
    def test_update_room(self):
        response = self.app.put('/rooms/1', json={"username": "JohnDoe", "room_name": "Updated Room"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Room updated successfully", response.get_data(as_text=True))
    
    def test_delete_room(self):
        response = self.app.delete('/rooms/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Room deleted successfully", response.get_data(as_text=True))
    
    def test_create_device(self):
        response = self.app.post('/devices', json={"username": "JohnDoe", "device_type": "Light", "house_id": 1})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Device created successfully", response.get_data(as_text=True))
    
    def test_get_devices(self):
        response = self.app.get('/devices')
        self.assertEqual(response.status_code, 200)
    
    def test_update_device(self):
        response = self.app.put('/devices/1', json={"username": "JohnDoe", "device_type": "Thermostat", "house_id": 1})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Device updated successfully", response.get_data(as_text=True))
    
    def test_delete_device(self):
        response = self.app.delete('/devices/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Device deleted successfully", response.get_data(as_text=True))
    
if __name__ == '__main__':
    unittest.main()
