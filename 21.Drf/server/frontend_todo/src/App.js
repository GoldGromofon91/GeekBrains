import React from 'react';
import axios from 'axios';
import './App.css';
import CreatorList from "./components/creator";
import ProjectList from "./components/project";
import TodoList from "./components/todo";
import {BrowserRouter, Route,Link, Switch} from "react-router-dom";
import ProjectInfo from "./components/projectinfo";


const server = {
    creators: "http://127.0.0.1:8000/api/creators/",
    projects: "http://127.0.0.1:8000/api/projects/",
    todo: "http://127.0.0.1:8000/api/todo/"
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
    constructor(parametrs) {
        super(parametrs)
        this.state = {
            'creators': [],
            'projects': [],
            'todo': [],
        }
    }

    componentDidMount() {
        axios
            .get(server.creators)
            .then(serv_response => {
                const response_data = serv_response.data
                this.setState(
                    {"creators": response_data}
                )
            })
            .catch(err => {
                console.log(err)
            });
        axios
            .get(server.projects)
            .then(serv_response => {
                const response_data = serv_response.data['results']
                this.setState(
                    {"projects": response_data}
                )
            })
            .catch(err => {
                console.log(err)
            });
        axios
            .get(server.todo)
            .then(serv_response => {
                const response_data = serv_response.data
                this.setState(
                    {"todo": response_data['results']}
                )
            })
            .catch(err => {
                console.log(err)
            });
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
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path={'/'} component={MainPage}/>
                        <Route exact path={'/projects/'} component={() => <ProjectList items={this.state.projects}/>}/>
                        <Route exact path={'/creators/'} component={() => <CreatorList creators={this.state.creators}/>}/>
                        <Route exact path={'/todo/'} component={() => <TodoList items={this.state.todo}/>}/>
                        <Route exact path={'/project/:id/'} component={() => <ProjectInfo items={this.state.projects}/>}/>
                        <Route component={PageNotFound}/>
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
