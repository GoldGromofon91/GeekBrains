import React from 'react';
import axios from 'axios';
import './App.css';
import CreatorList from "./components/creator";
import ProjectList from "./components/project";
import TodoList from "./components/todo";
import {BrowserRouter, Route, Link, Switch} from "react-router-dom";
import ProjectInfo from "./components/projectinfo";
import AuthorizationForm from "./components/login";
import Cookies from 'universal-cookie';
import ProjectCreateForm from "./components/ProjectCreateForm";
import TodoCreateForm from "./components/TodoCreateForm";

const server = {
    creators: "http://127.0.0.1:8000/api/creators/",
    projects: "http://127.0.0.1:8000/api/projects/",
    todo: "http://127.0.0.1:8000/api/todo/",
    token: "http://127.0.0.1:8000/api-token/",
    jwt: "http://127.0.0.1:8000/api/token/jwt/"
}
const PageNotFound = ({location}) => {
    return (
        <h1>Page at '{location.pathname}' not found</h1>
    )
}
const MainPage = () => {
    return (
        <h1>Hello custom Trello</h1>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            creators: [],
            projects: [],
            todo: [],
            token: '',
            refresh: ''
        }
    }

    getDataFromServer() {
        const headers = this.getHeaders()
        axios
            .get(server.creators, {headers})
            .then(serv_response => {
                const response_data = serv_response.data['results']
                // console.log(response_data)
                this.setState(
                    {"creators": response_data}
                )
            })
            .catch(err => {
                console.log(err)
                this.setState({creators: []})
            });
        axios
            .get(server.projects, {headers})
            .then(serv_response => {
                const response_data = serv_response.data['results']
                // console.log(response_data)
                this.setState(
                    {"projects": response_data}
                )
            })
            .catch(err => {
                console.log(err)
                this.setState({projects: []})
            });
        axios
            .get(server.todo, {headers})
            .then(serv_response => {
                const response_data = serv_response.data
                // console.log(response_data)
                this.setState(
                    {"todo": response_data['results']}
                )
            })
            .catch(err => {
                console.log(err)
                this.setState({todo: []})
            });
    }

    setToken(token) {
        const cookies = new Cookies()
        cookies.set('projectCookie', token)
        this.setState(
            {
                token: token
            },
            () => this.getDataFromServer()
        )
    }


    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.setToken('')
        // this.state.token = ''
    }

    getTokenAfterClose() {
        const cookie = new Cookies()
        const token = cookie.get('projectCookie')
        this.setState(
            {
                token: token
            },
            () => this.getDataFromServer()
        )
    }

    getToken(username, password) {
        axios.post(server.jwt, {username: username, password: password})
            .then(response => {
                this.setToken(response.data['access'])
                this.state.refresh = response.data['refresh']
            })
            .catch(error => alert('Неверный логин или пароль'))
    }

    getHeaders() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = `Bearer ${this.state.token}`;
        }
        return headers
    }

    componentDidMount() {
        this.getTokenAfterClose()

    }

    projectDelete(id) {
        const headers = this.getHeaders();
        axios
            .delete(server.projects + `${id}/`, {headers})
            .then(result => {
                this.setState({
                    projects: this.state.projects.filter((elem) => elem.id !== id)
                })
            })
            .catch(error => console.log(error))
    }

    projectCreate(projectName, authorId) {
        const headers = this.getHeaders();
        axios
            .post(server.projects,
                {name: projectName, users: [authorId]},
                {headers})
            .then(result => {
                console.log(result.data)
                const newProject = result.data;
                this.setState({
                    books: [...this.state.projects, newProject]
                })
            })
            .catch(error => console.log(error))
    }

    todoDelete(id) {
        console.log(id)
        const headers = this.getHeaders();
        axios
            .delete(server.todo + `${id}/`, {headers})
            .then(result => {
                console.log(this.state.todo)
                let new_todo = this.state.todo.filter((elem) => elem.id !== id)
                this.setState({
                    todo: new_todo
                })
                console.log(this.state.todo)
            })
            .catch(error => console.log(error))
    }

    todoCreate(projectId, authorId, todoText) {
        const headers = this.getHeaders();
        console.log(projectId, authorId, todoText)
        axios
            .post(server.todo,
                {project: projectId, user: authorId, text: todoText},
                {headers})
            .then(result => {
                console.log(result.data)
                const newTodo = result.data;
                this.setState({
                    books: [...this.state.todo, newTodo]
                })
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <nav className={'Menu'}>

                        <ul>
                            <li>
                                <Link className={'Link'} to={'/'}>Main</Link>
                            </li>
                            <li>
                                <Link className={'Link'} to={'/projects/'}>Projects</Link>
                            </li>
                            <li>
                                <Link className={'Link'} to={'/creators/'}>Users</Link>
                            </li>
                            <li>
                                <Link className={'Link'} to={'/todo/'}>Todo</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                    <Link className={'Link'} to={'/login/'}>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path={'/'} component={MainPage}/>
                        <Route exact path={'/projects/'} component={() =>
                            <ProjectList
                                items={this.state.projects}
                                deleteProject={(id) => this.projectDelete(id)}
                            />}
                        />
                        <Route exact path={'/projects/create'}>
                            <ProjectCreateForm
                                projectCreate={(projectName, authorId) => this.projectCreate(projectName, authorId)}
                                creators={this.state.creators}/>
                        </Route>
                        <Route exact path={'/creators/'}
                               component={() =>
                                   <CreatorList creators={this.state.creators}/>}
                        />
                        <Route exact path={'/todo/'} component={() => <TodoList items={this.state.todo}
                                                                                deleteTodo={(id) => this.todoDelete(id)}/>}/>
                        <Route exact path={'/todo/create'}>
                            <TodoCreateForm
                                todoCreate={(projectId, authorId, todoText) => this.todoCreate(projectId, authorId, todoText)}
                                creators={this.state.creators}
                                projects={this.state.projects}/>
                        </Route>
                        <Route exact path={'/project/:id/'}
                               component={() =>
                                   <ProjectInfo items={this.state.projects}/>}
                        />
                        <Route exact path={'/login/'}>
                            <AuthorizationForm getToken={(username, password) => this.getToken(username, password)}/>
                        </Route>
                        <Route component={PageNotFound}/>
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
