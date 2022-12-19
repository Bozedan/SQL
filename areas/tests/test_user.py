import pytest
from controller.user_controller import UserController
from  jwt import decode

class TestUser:

	def test_regestration_not_exists(self):
		user_contoller = UserController()
		result = user_contoller.signupStudent('tester', 'abc123')
		assert result == True
	
	def test_regestration_exists(self):
		user_contoller = UserController()
		result = user_contoller.signupStudent('tester', 'abc123')
		result = user_contoller.signupStudent('tester', 'abc123')
		assert result == False
	
	def test_regestration_exists(self):
		user_contoller = UserController()
		result = user_contoller.signupStudent('tester', 'abc123')
		result = user_contoller.signupStudent('tester', 'abc123')
		assert result == False
	
	def test_authorize_access(self):
		user_contoller = UserController()
		user_contoller.signupStudent('tester', 'abc123')
		token = user_contoller.authorize('tester', 'abc123')
		user = user_contoller.user_service.user_repository.db.get_user_by_id(decode(token, "a random, long, sequence of characters that only the server knows", ["HS256"])['id']).get_username()
		assert user == 'tester'
	
	def test_authorize_not_access(self):
		user_contoller = UserController()
		user_contoller.signupStudent('tester', 'abc123')
		user = user_contoller.authorize('tester', 'abc12345')
		assert user == None
	
	def test_user_deleted(self):
		user_contoller = UserController()
		user_contoller.signupStudent('tester', 'abc123')
		user = user_contoller.authorize('tester', 'abc123')
		result = user_contoller.delete_account(user)
		assert result == True

	def test_moderator_registration_not_exists(self):
		user_controller = UserController()
		result = user_controller.signup_moderator('tester', 'abc123')
		assert result == True

	def test_moderator_registration_exists(self):
		user_controller = UserController()
		user_controller.signup_moderator('tester', 'abc123')
		result = user_controller.signup_moderator('tester', 'abc123')
		assert result == False

	def test_teacher_registration_not_exists(self):
		user_controller = UserController()
		result = user_controller.signup_teacher('tester', 'abc123')
		assert result == True

	def test_teacher_registration_exists(self):
		user_controller = UserController()
		user_controller.signup_teacher('tester', 'abc123')
		result = user_controller.signup_teacher('tester', 'abc123')
		assert result == False

	def test_edit_login(self):
		user_controller = UserController()
		res, id = user_controller.signup_moderator('tester', 'abc123')
		res = user_controller.edit_user_profile(id, 'tester1', None)
		assert res == True

	def test_edit_password(self):
		user_controller = UserController()
		res, id = user_controller.signup_moderator('tester', 'abc123')
		res = user_controller.edit_user_profile(id, None, 'abc1234')
		assert res == True
