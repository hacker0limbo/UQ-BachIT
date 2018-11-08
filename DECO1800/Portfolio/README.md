# Instructions for My Portfolio

All files are in the `dist` folder, and it contains all the compiled files(Since i used `vuepress` library).

## Run my Website
The website could not be directly run in a browser since it is a `SPA` and using `router` to manage different pages' path. It requires a `static file server`. To run my portfolio, there are serveral options to implement:

- I have deployed my portfolio to my [github page](https://hacker0limbo.github.io/). Just check the link here.
- You can open it by running a local statc file server. I recommend using [anywhere](https://www.npmjs.com/package/anywhere). It is a npm module, so first make sure you installed `node.js` on your laptop. Below are the code to do this:
    ```bash
    npm install anywhere -g # install anywhere

    cd dist # locate to dist folder
    anywhere # anywhere will automatically find index.html and render it
    ```
- You could also check the vuepress [documentation](https://vuepress.vuejs.org/guide/getting-started.html). I have set the dependency, so all you have to do is:

    ```bash
    cd project
    npm run docs:dev # go to localhost:8080
    
    npm run docs:build # generate static assets
    ```