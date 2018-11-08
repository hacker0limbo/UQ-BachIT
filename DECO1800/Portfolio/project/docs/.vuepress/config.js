module.exports = {
    title: "My Portfolio",
    description: 'Portfolio for The Age Old',
    plugins: ['@vuepress/back-to-top'],
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Guide', link: '/guide/' },
            {
                text: 'Project',
                items: [
                    { text: 'Project A', link: '/Project/ProjectA' },
                    { text: 'Project B', link: '/Project/ProjectB' },
                    { text: 'Project C', link: '/Project/ProjectC' },
                ]
            },
            { text: 'Reflection', link: '/reflection/' }
        ],
    },
    markdown: {
        lineNumbers: true
    },

}