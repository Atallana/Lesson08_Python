import requests


url = "https://ru.yougile.com/api-v2/"

headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 5k0_IqvN0t0lYfbkK58_CVnueBntItdio1O3uvF8a39T0HsJHsRM5vPzeweafeom"
        }

def test_get_project(): 
    """Позитивный тест "Получить по ID"""
    # Создаем проект
    project = {
        "title": "Новый проект"
    }
     
    response = requests.post(f"{url}projects", json=project, headers=headers)

    assert response.status_code == 201

    # Получаем ID созданного проекта
    response_body = response.json()
    id = response_body["id"]

    # запрашиваем проект по ID
    response = requests.get(f"{url}projects/{id}", headers=headers)

    assert response.status_code == 200

def test_get_negative(): 
    """Негативный тест "Получить по ID"""
    id = "qwerty"

    # запрашиваем проект по ID
    response = requests.get(f"{url}projects/{id}", headers=headers)

    assert response.status_code == 404

def test_create_project():
    """Позитивный тест "Создать"""
    # Создаем проект
    title = "Создание проекта"
    project = {
        "title": f"{title}"
    }
        
    response = requests.post(f"{url}projects", json=project, headers=headers)

    assert response.status_code == 201

    # Получаем ID созданного проекта
    response_body = response.json()
    id = response_body["id"]

    # запрашиваем проект по ID
    response = requests.get(f"{url}projects/{id}", headers=headers)

    assert response.status_code == 200

    response_body = response.json()
    title_new = response_body["title"]

    assert title_new == title

def test_create_negative():
    """Негативный тест "Создать"""
    # Создаем проект
    title = ""
    project = {
        "title": f"{title}"
    }
        
    response = requests.post(f"{url}projects", json=project, headers=headers)

    assert response.status_code == 400

def test_update_project():
    """Позитивный тест "Изменить"""
     # Создаем проект
    title = "Создание проекта"
    project = {
        "title": f"{title}"
    }
        
    response = requests.post(f"{url}projects", json=project, headers=headers)

    assert response.status_code == 201

    # Получаем ID созданного проекта
    response_body = response.json()
    id = response_body["id"]

    # редактируем 
    new_title = "Отредактированный проект"
    project = {
        "title": f"{new_title}"
    }

    response = requests.put(f"{url}projects/{id}", json=project, headers=headers)

    assert response.status_code == 200

    # запрашиваем по ID 
    response = requests.get(f"{url}projects/{id}", headers=headers)

    assert response.status_code == 200

    response_body = response.json()
    title_from_response = response_body["title"]

    assert title_from_response == new_title

def test_update_negative():
    """Негативный тест "Изменить"""
     # Создаем проект
    title = "Создание проекта"
    project = {
        "title": f"{title}"
    }
        
    response = requests.post(f"{url}projects", json=project, headers=headers)

    assert response.status_code == 201

    # Получаем ID созданного проекта
    response_body = response.json()
    id = response_body["id"]

    # редактируем 
    new_title = ""
    project = {
        "title": f"{new_title}"
    }

    response = requests.put(f"{url}projects/{id}", json=project, headers=headers)

    assert response.status_code == 400

    # запрашиваем по ID 
    response = requests.get(f"{url}projects/{id}", headers=headers)

    assert response.status_code == 200

    response_body = response.json()
    title_from_response = response_body["title"]

    assert title_from_response == title
