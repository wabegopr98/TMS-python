url = 'http://localhost:5000/api'
docker_url_api = 'http://web:5000/api'

url_ui = 'http://localhost:5000/login'
docker_url_ui = 'http://web:5000/api'
cabinet_url = 'http://localhost:5000/tasks'


#docker-compose build
#docker-compose run --rm -e TEST_PATH=tests/api/tests/test_register_user.py -e TEST_ARGS='--alluredir=allure' test