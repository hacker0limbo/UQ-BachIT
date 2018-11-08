---
sidebar: auto
prev: ../
next: ../Project/ProjectA.md
---

<style>
    p, ul {
        font-family: "Georgia";
    }

</style>

# Guide

## About Me
My name is Weiting Yin, i am now doing Bachelor of IT at UQ. I am interested in both front-end and back-end develop. I work with my group in DECO1800 as a <span>developer</span>.


Below are my personal technical skills for Web Development:

### Front-End

- HTML ![html](../images/html.png)
    - [pug.js](https://pugjs.org/api/getting-started.html)
- CSS ![css](../images/css.png)
    - [less.js](http://lesscss.org/)
- JavaScript ![js](../images/javascript.png)
    - ES5 / ES6
    - [JQuery](https://jquery.com/) ![jquery](../images/jquery.png)
    - [Vue.js](https://vuejs.org/index.html) ![vue](../images/vue.png)

### Back-end

- Python ![py](../images/python.png)
    - [Flask](http://flask.pocoo.org/)
- Node.js ![node](../images/node.png)
    - [Express.js](https://expressjs.com/)


## About This Website

I designed this website using [VuePress](https://vuepress.vuejs.org). It is a `SPA` website, powered by [Vue](https://vuejs.org/), [Vue Router](https://github.com/vuejs/vue-router) and [webpack](https://webpack.js.org/). It provides users great user-experiencing since part of pages will be loaded depend on user's demand, user will not feel any page loading delay.

The main goal of `vuepress` is that, we first write markdown code and `vuepress` will help to `compile` and `render` them into html. In this way, we could focus more on content itself rather than designing.

### Why

The reason why i choose this tool is that, i know a little bit about `vue.js`, and vue community provides such a great tool to help writing documentation. Also, i am quite familiar with [markdown](https://en.wikipedia.org/wiki/Markdown). Futher, `vuepress` allowing user to insert vue `component` into markdown file, thus it is powerful to custom personal theme and plugins

### Run

There are serveral options to run this application:

::: warning
Since vuepress requires node.js version >= 8, I highly recommend just go to my github page to check the demo, link is listed below.
:::

1. I have already `deployed` my portfolio to `github pages`. Feel free to check it [here](https://hacker0limbo.github.io/)


2. install `vuepress` through `npm` or `yarn`, detailed information are listed on officiall website. Once installed, execuate following command in terminal:
   
    ```bash
    # make sure first you have package.json with relative command on your root project
    npm run docs:dev # or yarn docs:dev
    # then you are able to see the whole project and even do some changes!
    ```

3. Using `static file server`. I recommend using [anywhere](https://www.npmjs.com/package/anywhere). It would easily generate a static file server based on your root project with just one line of code. However, before doing that, you have to `compile` markdown file to html file. Below are complete code to do that:

    ```bash
    # install anywhere using npm
    npm install anywhere -g

    # build files, all the compiled files are added into vuepress/dist folder
    npm run docs:build

    # locate to dist directory
    # start server
    cd .vuepress/dist
    $ anywhere
    ```    

## About My Team

Our team is called **The Age Old**, we have 4 members with 2 developers and 2 designers. We are aiming to build a educational website for children related with bribane history

### Team Members

Our team members and their positions in this team are listed in a table below:

| Name          | Identity      |  Contribution  |
|---------------|---------------|----------------|
| Matt          | Leader        | Leading team   |
| Even          | Designer      | html & css     |
| Fleur         | Designer      | html & css     |
| Stephen       | Developer     | JavaScript     |

### Personal Contribution

Since I am not good at design and report writing, i am responsible for develop work, more specifically, work that is realted with `JavaScript`.

Generally what i did for my team are:
- Use `ajax` to pull data and store them locally
- Writing `Conpoments` for our website
- Using third party library to do interactive effects for our page
- Code Refactoring
- Answer technical related questions when doing presentation

::: tip NOTE
Detailed information about my personal contribution will be introduced in Project Page.
:::


