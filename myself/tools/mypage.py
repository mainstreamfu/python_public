

class MyPage(object):
    def __init__(self,page_num,total_count,base_url,per_page_num=10,max_show=3):
        '''
        :param page_num: 当前页
        :param total_count: 数据总数
        :param base_url: 分页页码跳转的url
        :param per_page_num: 每一页显示多少条数据
        :param max_show: 页面上最多显示多少页码
        '''
        #实例化传进来的参数
        self.page_num = page_num
        self.total_count = total_count
        self.base_url = base_url
        self.per_page_num = per_page_num
        self.max_show = max_show
        #根据传进来的参数，计算几个值
        try:
            self.page_num = int(page_num)
        except Exception as e:
            self.page_num = 1

        self.half_show = int((self.max_show - 1) / 2)

        # 总共有多少页
        self.total_page_num, more = divmod(self.total_count, self.per_page_num)
        if more:
            self.total_page_num += 1

    @property
    def start(self):
        return (self.page_num - 1) * self.per_page_num

    @property
    def end(self):
        return self.page_num * self.per_page_num

    def page_html(self):


        '''
        返回页面上可以用的一段HTML
        一段可用的分页页码的HTML
        '''
        page_start = self.page_num - self.half_show
        # 页面上页码最多展示到哪一个
        page_end = self.page_num + self.half_show
    # 如果当前页小于等于half_show, 默认从第一页展示到max_show
        if self.page_num <= self.half_show:
            page_start = 1
            page_end = self.max_show
        # 如果当前页大于等于总页数-half_show
        if self.page_num >= self.total_page_num - self.half_show:
            page_end = self.total_page_num
            page_start = self.total_page_num - self.max_show+1

        # 生成前页码的HTML
        page_html_list = []
        # 放置一个首页按钮
        page_first_tmp =  '<li><a href="{}?page=1">首页</a></li>'.format(self.base_url)
        page_html_list.append(page_first_tmp)

        # 加上一页按钮
        if self.page_num - 1 <= 0:  # 表示没有上一页
            page_prev_tmp = '<li class="disabled" ><a href="#">上一页</a></li>'
        else:
            page_prev_tmp = '<li><a href="{0}?page={1}">上一页</a></li>'.format(self.base_url,self.page_num - 1)
        page_html_list.append(page_prev_tmp)

        for i in range(page_start, page_end+1):
            # 如果是当前页，就加一个active的样式
            if i == self.page_num:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url,i)
            else:
                tmp = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url,i)
            page_html_list.append(tmp)
        if self.page_num+1 > self.total_page_num:
            page_next_tmp = '<li class="disabled"><a href="#">下一页</a></li>'
        else:
            page_next_tmp = '<li><a href="{0}?page={1}">下一页</a></li>'.format(self.base_url,self.page_num+1)
        page_html_list.append(page_next_tmp)
        page_last_tmp = '<li><a href="{0}?page={1}">尾页</a></li>'.format(self.base_url,self.total_page_num)
        page_html_list.append(page_last_tmp)
        return "".join(page_html_list)

