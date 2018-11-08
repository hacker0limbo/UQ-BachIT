---
sidebar: auto
prev: ../Project/ProjectC.md
---

<style>
    p, ul {
        font-family: "Georgia";
    }

</style>

# Reflection
It is a great experience taking this course, our team successfully finished our website and and did a good job for our trade show. However, there still exists some points that we could improve in the future, i will address those part following.

## Expectations

### Fulfill
When looked back to my journal post and our group's todo list, we completed about 90% of our initial plans. Here are things that we finished:

- Complete the website and put it on the server
    - Interact with data API
    - No serious bugs
    - Page style is accorded with old newspaper style
    - Responsive design
    - Leave necessary comments for the code
    - Added css animation making it more interactive

- Did a good job for the **trade show**
    - Got No.5 of *Most welcome website*
    - Presentation and pitch goes well
    - Other students and tutors are interested with our website

### Remain
However, there are still some functions where we did not accomplish. Mostly this is because of time limits.

- `War` game did not interactive with data
- `Flip book` remians little layout issue
- `Convict` part did not contains any data
- `Typing effects` only shows one line of text, better to be mutiple lines

### Improvement
Except the points i mentioned above, some parts of our project could still be improved or upgraded.

- Using [require.js](https://requirejs.org/) to do the module loader.
- Image `preload`
- Using `vue.js` to write the whole page
- Code refactoring
    - Using [less.js](http://lesscss.org/) for `css` refactor
    - Using [pug.js](https://pugjs.org/api/getting-started.html) for `html` refactor
    - Using [typescript](https://www.typescriptlang.org/) for `javascript` refactor

#### Require.js
There is a big issure for our code. If we want to use a library in different pages, we have to link that library to all pages, this is unefficient. Futhermore, considering linked files are globally, which means functions that have been defined are all `global`. It is possible that we rewrite that function in another different file. Therefore, it is important to use module to manage our functions. `require.js` is meant for doing this.

`require.js` is a JavaScript file and **module loader**. It is optimized for in-browser use and follows `AMD` rules.

One of the aims of `require.js` is that, you could load your module by demand, for example, if your script only need moduleA, you could choose just load moduleA, moduleB will not be loaded.

Here is an example of using `require.js`:

```js
/*
File structure looks like this:

project-directory/
    project.html
    scripts/
        main.js
        require.js
        helper/
            util.js

In your main.js file, i want to load util.js
 */

require(["helper/util"], function(util) {
    // do something with util module
});

```

#### Image preload
Another bing issue of our website is, our page includes a lot of images and loading them dynamicly may delay rendering the page, therefore, we need such a technique called **image preload**.

Preloading images is a great way to improve the user experience. When images are preloaded in the browser, the visitor can surf around your site and enjoy extremely faster loading times.

There are several ways to do this, here i am just going to use `promise` to address this problem.

```js
const preLoadImg = (source) => {
    let pr = [];
    source.forEach((url) => {
        let p = loadImage(url)
            .then(img => this.images.push(img))
            .catch(err => console.log(err))
        pr.push(p);
    })

    Promise.all(pr)
        .then(() => {
            // do sth
        });
}

const loadImage = (url) => {
    return new Promise((resolve, reject) => {
        let img = new Image();
        img.onload = () => resolve(img);
        img.onerror = reject;
        img.src = url;
    })
}
```

## Reap
Basically i learned a lot from this course, it is a great course and i think it helped me in my way of web development.

### Team work
I met a good team, all my members contributed a lot to this project, we have a good team environmnet, and no one had complian thier task. We cleared division of work. Also, all my team members are eager to help each other, we sloved problems together and this is how we push our team progress ahead.

### Communication
Since i am not a native English-speaker, but the other members are all native speakers. We need to communicate a lot during the work. This helped me to practice my english skills and my communication skills as well. Since everyone is busy, you must explain you problem fast and clear. Luckily, all my group members are patient, even thought sometimes i did not state my confusion clearly, they still guide me and try to lead me in the right way of our group progress.

### Workshop
In the workshop tutors taught some useful library and skills suchs as `php`, i did not use too much about what i learned from the workshop. Once you have a strong language foundamentals, it is easy to read the documentation and use that library. However, it is still good to know those libraries.

### Time management
It is necessary to have good time management, since i am also taking other courses, it is important to know how to balance your time with different cources separately. Therefore, in my group, after work distribution, leader would confirm what is the suitable time to submit our individual work to make sure no one will delay. There are some features because of bad time management, but most of the time, we are on the right track.

## Individual Improvement
It is still a long way to go to become a web developer, self development and independent study is important for future development.

In the future, i plan to focus on learing one framework `Vue.js`, and keep improving my `javascript` skills as well. Since `es8` is going to release, i can not fall behind.

Additionally, since i learnd `csse1001` this semester, i plan to learn one backend framework `flask` as well, also, `node.js` will be covered in the future.

<br>
<br>
<br>
<img src="../images/finish.png" style="float: right">
