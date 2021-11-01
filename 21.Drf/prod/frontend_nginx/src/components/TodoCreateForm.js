import React from "react";

class TodoCreateForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            projectId: 1,
            authorId: 1,
            todoText: ''
        }
    }

    handlerOnInput(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handlerOnSubmitForm(event) {
        console.log(event.target.value)
        this.props.todoCreate(this.state.projectId, this.state.authorId, this.state.todoText)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handlerOnSubmitForm(event)}>
                <select name="projectId"
                        onChange={(event) => this.handlerOnInput(event)}>
                    {this.props.projects.map((elem) => (
                        <option value={elem.id} key={elem.id}>
                            {elem.name}
                        </option>
                    ))}
                </select>

                <select name="authorId"
                        onChange={(event) => this.handlerOnInput(event)}>
                    {this.props.creators.map((author) => (
                        <option value={author.id} key={author.id}>
                            {author.username}
                        </option>
                    ))}
                </select>

                <input type="text" name={"todoText"} placeholder={"Todo text"}
                       onChange={(event) => this.handlerOnInput(event)}/>
                <input type="submit" value="Create"/>
            </form>
        )
    }
}

export default TodoCreateForm