from app import app # From the folder app import the variable app
import config


if __name__ == "__main__":
    app.run(debug=True)
