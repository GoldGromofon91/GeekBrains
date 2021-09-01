import React from 'react';
import logo from './logo.svg';
import './App.css';
import CreatorList from "./components/creator";
import axios from 'axios';
import './CONST';

class App extends React.Component {
   constructor(parametrs) {
       super(parametrs)
       this.state = {
           'creators': []
       }
   }
   componentDidMount() {
       axios
           .get('http://127.0.0.1:8000/api/creators/')
           .then(serv_response =>{
               const response_data = serv_response.data['results']
               console.log(response_data)
               this.setState(
                   {"creators":response_data}
               )
           })
           .catch(err =>{console.log(err)})
   }
   render () {
       return (
           <div id="root">
               <header>MENU</header>
               <div id="content">
                   <CreatorList creators={this.state.creators}/>
               </div>
               <footer>FOOTER</footer>
           </div>
       )
   }
}
export default App;
