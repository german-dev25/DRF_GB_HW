import React from 'react';
import Axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/UserList.js';
import ProjectsList from './components/ProjectsList.js';
import TodosList from './components/TodosList.js';
import axios from 'axios';
import {HashRouter, Route, BrowserRouter, Routes, Link, Navigate, useLocation } from 'react-router-dom'

class App extends React.Component {

    constructor (props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        }
    }

componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users').then(response => {
        const users = response.data.results
            this.setState(
                {
                    'users': users
                }
            )
    }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/projects').then(response => {
        const projects = response.data.results
            this.setState(
                {
                    'projects': projects
                }
            )
    }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/todos').then(response => {
        const todos = response.data.results
            this.setState(
                {
                    'todos': todos
                }
            )
    }).catch(error => console.log(error))
}

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Список Todo</Link></li>
                        <li><Link to='/projects'>Список проектов</Link></li>
                        <li><Link to='/users'>Список пользователей</Link></li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element = { <TodosList todos={this.state.todos} /> } />
                        <Route exact path='/projects' element = { <ProjectsList projects={this.state.projects} /> } />
                        <Route exact path='/users' element = { <UserList users={this.state.users} /> } />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
