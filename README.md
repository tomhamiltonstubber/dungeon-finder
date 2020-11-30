![CI](https://github.com/tomhamiltonstubber/dungeon-finder/workflows/CI/badge.svg)

# Dungeon Finder

Dungeon Finder (TBC) will be a web app built by @codetopixels and @tomhamiltonstubber to provide an easy way for 
Dungeons & Dragons players to match with Game Masters (also known as Dungeon Masters, or DMs for short). 
Players will be able to view a list of games that have been created by DMs, filterable by a number of 
different attributes. Players will then be able to rate and review their DM.

Builkt with [FastAPI](https://fastapi.tiangolo.com/).

## To run locally

Create a virtualenv and install requirements with `make install-dev`.

To run the server navigate to `src` and run `uvicorn main:app --reload`. Changes to the code 
will cause the app to rebuild so you don't need to worry.

If you haven't created the database yet you can do `make reset-db` to create it.

To load and watch static files (JS/SCSS) for changes, run `yarn-watch`. When you're running for the first time, run 
`yarn install`. The SCSS files in `static/scss/` will be compiled into `.css` files in `static/dist`. JavaScript in `static/js` 
will be compiled and minified into `static/dist`.
