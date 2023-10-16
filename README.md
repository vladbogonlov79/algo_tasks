# Задачи по программированию 

## Структура проекта:


## Как работать с гитом?

Для начала делаешь fork через github и клонируешь свой получившийся репозиторий

```git clone <repo>```

### Как подтягивать обновления, сделанные мной?

Добавь мой репозиторий как upstream к своему локальному (делать только первый раз):

```git remote add upstream <original_repo>```


Забери изменения

```git pull upstream master```

Закинь изменения на свой форкнутый репозиторий: 

 ```git push origin master```

### Как добавлять изменения?

Ты можешь работать сразу на нескольких ветках, например, если pull request с прошлой ветки я еще не проверил, чтобы создать ветку нужно сначала переключиться на основную:

```git checkout master```

потом уже создать новую ветку

```git checkout -b <branch_name>```

Сделай изменения и запушь 

```git add <files>```

```git commit -m <comment>```

```git push --set-upstream origin <branch_name>```

## Как делать pull request?

[Инструкция](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
