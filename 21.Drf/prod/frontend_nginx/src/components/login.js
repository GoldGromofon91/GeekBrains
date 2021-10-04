import React from "react";

class AuthorizationForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        }
    }

    handlerOnInput(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handlerOnSubmitForm(event) {
        // console.log(this.state)
        this.props.getToken(this.state.username,this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handlerOnSubmitForm(event)}>
                <input type="text" name={"username"} placeholder={"username"} onChange={(event) => this.handlerOnInput(event)}/>
                <input type="password" name={"password"} placeholder={"password"} onChange={(event) => this.handlerOnInput(event)}/>
                <input type="submit" value="login"/>
            </form>
        )
    }
}

export default AuthorizationForm