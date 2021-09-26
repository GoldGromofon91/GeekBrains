# Список авторов с их количеством
query{
  allAuthors{
    allCountAuthor
    edges{
      node{
        username,
        isSuperuser,
        birthdayYear
      }
    }
  }
}
# Поиск пользователя по имени
query{
  authorByName(name:"dj"){
    username
  }
}
# Показ списка пользователей с Проектами и заметками
query{
	allAuthorInProject{
    id
    username,
    project{
      id
      name
    },
    userTodo{
      id,
      text
    }
  }
}