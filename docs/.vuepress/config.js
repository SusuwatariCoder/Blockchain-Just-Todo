// 配置文件

module.exports = {
    title: '区块链-学习-实践',
    description: 'Just to do something by Blockchain',
     // 路径
    base: '/Blockchain-Just-Todo/',
    themeConfig: {
        // 导航栏配置
        logo: '/logo.png',
        nav: [
            // 导航栏链接
            { text: '首页', link: '/' },
            { text: '资源', link: '/links/' },
            { text: 'Github', link: 'https://github.com/SusuwatariCoder/Blockchain-Just-Todo' },
          ],
        // 侧边栏
        sidebar: [
<<<<<<< HEAD
          {
            title: '学习比特币',   // 必要的
            path: '/bitcoin/',      // 可选的, 标题的跳转链接，应为绝对路径且必须存在
            collapsable: true, // 可选的, 默认值是 true,
            sidebarDepth: 1,    // 可选的, 默认值是 1
            children: []
            },
            {
              title: '学习以太坊',   // 必要的
              path: '/ethereum/',      // 可选的, 标题的跳转链接，应为绝对路径且必须存在
              collapsable: true, // 可选的, 默认值是 true,
              sidebarDepth: 1,    // 可选的, 默认值是 1
              children:  []
              },
          ],
=======
            ['/', '学习实践 区块链'],
        ],
>>>>>>> 2db7679b9ed9b164dab0b0fc3010e696ac6862d7
        // 更新时间
        lastUpdated: '最近更新', 
    

      }
}