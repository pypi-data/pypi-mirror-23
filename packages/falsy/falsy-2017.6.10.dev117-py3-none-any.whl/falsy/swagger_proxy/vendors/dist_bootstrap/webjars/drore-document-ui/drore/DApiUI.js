/**
 * Created by xiaoym on 2017/4/17.
 */

var dapi = (function ($, api_url) {
    //初始化类
    var DApiUI = {};

    DApiUI.init = function () {
        $.ajax({

            url: api_url,//"/test/demo_simple_spec.json",
            // url:"/v2/api-docs",
            // url: "1.json",
            dataType: "json",
            type: "get",
            async: false,
            success: function (data) {
                //var menu=JSON.parse(data)
                var menu = data;
                console.log(menu);
                DApiUI.createDescription(menu);
                DApiUI.initTreeMenu(menu);
                DApiUI.eachPath(menu);
            }
        })
    }


    /***
     * 创建面板
     */
    DApiUI.creatabTab = function () {
        var divcontent = $('<div id="myTab" class="tabs-container" style="width:95%;margin:0px auto;"></div>');

        var ul = $('<ul class="nav nav-tabs"></ul>')
        var liapi = $('<li><a data-toggle="tab" href="#tab1" aria-expanded="false"> 接口说明</a></li>');
        ul.append(liapi);
        var lidebug = $('<li class=""><a data-toggle="tab" href="#tab2" aria-expanded="true"> 在线调试</a></li>');
        ul.append(lidebug);

        divcontent.append(ul);

        var tabcontent = $('<div class="tab-content"></div>');
        var tab1content = $('<div id="tab1" class="tab-pane"><div class="panel-body"><strong>接口详细说明</strong><p>Bootstrap 使用到的某些 HTML 元素和 CSS 属性需要将页面设置为 HTML5 文档类型。在你项目中的每个页面都要参照下面的格式进行设置。</p></div></div>');
        tabcontent.append(tab1content);
        var tab2content = $('<div id="tab2" class="tab-pane"><div class="panel-body"><strong>正在开发中,敬请期待......</strong></div></div>');
        tabcontent.append(tab2content);
        divcontent.append(tabcontent);

        //内容覆盖
        DApiUI.getDoc().html("");
        DApiUI.getDoc().append(divcontent);
        DApiUI.log("动态激活...")
        //liapi.addClass("active");
        DApiUI.log("动态激活12...")
        DApiUI.getDoc().find("#myTab a:first").tab('show')
        //$('#myTab a:first').tab('show')

    }


    /***
     * 创建简介table页面
     * @param menu
     */
    DApiUI.createDescription = function (menu) {
        var table = $('<table class="table table-hover table-bordered table-text-center"></table>');
        var thead = $('<thead><tr><th colspan="2" style="text-align:center">Swagger-Bootstrap-UI-前后端api接口文档</th></tr></thead>');
        table.append(thead);
        var tbody = $('<tbody></tbody>');
        var title = $('<tr><th class="active">项目名称</th><td style="text-align: left">' + menu.info.title + '</td></tr>');
        tbody.append(title);
        var description = $('<tr><th class="active">简介</th><td style="text-align: left">' + menu.info.description + '</td></tr>');
        tbody.append(description);
        var author = $('<tr><th class="active">作者</th><td style="text-align: left">' + menu.info.contact.name + '</td></tr>')
        tbody.append(author);
        var version = $('<tr><th class="active">版本</th><td style="text-align: left">' + menu.info.version + '</td></tr>')
        tbody.append(version);
        var host = $('<tr><th class="active">host</th><td style="text-align: left">' + menu.host + '</td></tr>')
        tbody.append(host)
        var service = $('<tr><th class="active">服务url</th><td style="text-align: left">' + menu.info.termsOfService + '</td></tr>')
        tbody.append(service);
        table.append(tbody);

        var div = $('<div  style="width:95%;margin:0px auto;"></div>')
        div.append(table);
        //内容覆盖
        DApiUI.getDoc().html("");
        DApiUI.getDoc().append(div);
        DApiUI.getDoc().data("data", menu);
    }

    /***
     * 初始化菜单树
     * @param menu
     */
    DApiUI.initTreeMenu = function (menu) {
        //遍历tags
        var tags = new Array();
        //简介li
        var dli = $('<li  class="active"><a href="javascript:void(0)"><i class="icon-text-width"></i><span class="menu-text"> 简介 </span></a></li>')
        dli.on("click", function () {
            DApiUI.log("简介click")
            DApiUI.createDescription(menu);
            dli.addClass("active");
        })
        DApiUI.getMenu().html("");
        DApiUI.getMenu().append(dli);
        var methodApis = DApiUI.eachPath(menu);

        $.each(menu.tags, function (i, tag) {
            var tagInfo = new TagInfo(tag.name, tag.description);
            //查找childrens
            $.each(methodApis, function (i, methodApi) {
                //判断tags是否相同
                if (methodApi.tag == tagInfo.name) {
                    tagInfo.childrens.push(methodApi);
                }
            })
            DApiUI.log("子标签数量:" + tagInfo.childrens.length);
            var len = tagInfo.childrens.length;
            if (len == 0) {
                var li = $('<li ><a href="javascript:void(0)"><i class="icon-text-width"></i><span class="menu-text"> ' + tagInfo.name + ' </span></a></li>');
                DApiUI.getMenu().append(li);
            } else {
                //存在子标签
                var li = $('<li></li>');
                var titleA = $('<a href="#" class="dropdown-toggle"><i class="icon-file-alt"></i><span class="menu-text">' + tagInfo.name + '<span class="badge badge-primary ">' + len + '</span></span><b class="arrow icon-angle-down"></b></a>');
                li.append(titleA);
                //循环树
                var ul = $('<ul class="submenu"></ul>')
                $.each(tagInfo.childrens, function (i, children) {
                    var childrenLi = $('<li class="menuLi"></li>');
                    var childrenA = $('<a href="javascript:void(0)"><i class="icon-double-angle-right"></i>' + children.summary + '</a>');
                    childrenLi.append(childrenA);
                    childrenLi.data("data", children);
                    ul.append(childrenLi);
                })
                li.append(ul);
                DApiUI.getMenu().append(li);
            }
        })
        DApiUI.log("菜单初始化完成...")
        DApiUI.initLiClick();
    }


    DApiUI.eachPath = function (menu) {
        var paths = menu.paths;
        DApiUI.log(paths);
        //paths是object对象,key是api接口地址,
        var methodApis = [];
        for (var key in paths) {
            var obj = paths[key];
            //遍历obj,获取api接口访问方式
            //八中方式类型,直接判断
            if (obj.hasOwnProperty("get")) {
                info = obj['get'];
                info['basePath'] = menu['basePath'];
                //get方式
                var apiInfo = new ApiInfo(info);
                apiInfo.methodType = "get";
                apiInfo.url = key;
                methodApis.push(apiInfo);
            }

            if (obj.hasOwnProperty("post")) {
                info = obj['post'];
                info['basePath'] = menu['basePath'];

                //post 方式
                var apiInfo = new ApiInfo(info);
                apiInfo.methodType = "post";
                apiInfo.url = key;
                methodApis.push(apiInfo);
            }
        }
        console.log(methodApis);
        return methodApis;

    }

    /***
     * li标签click事件
     */
    DApiUI.initLiClick = function () {
        DApiUI.getMenu().find(".menuLi").bind("click", function (e) {
            e.preventDefault();
            var that = $(this);
            var data = that.data("data");
            DApiUI.log("Li标签click事件");
            DApiUI.log(data);
            //获取parent-Li的class属性值
            var parentLi = that.parent().parent();
            DApiUI.log(parentLi);
            var className = parentLi.prop("class");
            DApiUI.log(className)
            DApiUI.getMenu().find("li").removeClass("active");
            //parentLi.addClass("active");
            that.addClass("active");
            DApiUI.createApiInfoTable(data);
            DApiUI.createDebugTab(data);
        })
    }

    DApiUI.getStringValue = function (obj) {
        var str = "";
        if (typeof (obj) != 'undefined' && obj != null) {
            str = obj.toString();
        }
        return str;
    }
    /**
     * 创建调试面板
     */
    DApiUI.createDebugTab = function (apiInfo) {
        DApiUI.log("创建调试tab")
        //方法、请求类型、发送按钮
        var div = $('<div style="width: 100%;margin: 0px auto;margin-top: 20px;"></div>');
        var headdiv1 = $('<div class="input-group m-bot15"><span class="input-group-btn"><button class="btn btn-default btn-info" type="button">' + DApiUI.getStringValue(apiInfo.methodType) + '</button></span><input type="text" id="txtreqUrl" class="form-control" value="' + DApiUI.getStringValue(apiInfo.url) + '"/><span class="input-group-btn"><button id="btnRequest" class="btn btn-default btn-primary" type="button"> 发 送 </button></span></div>');
        div.append(headdiv1);


        //请求参数
        var divp = $('<div class="panel panel-primary"><div class="panel-heading">请求参数</div></div>')

        var divpbody = $('<div class="panel-body"></div>')
        //判断是否有请求参数
        if (typeof (apiInfo.parameters) != 'undefined' && apiInfo.parameters != null) {
            var table = $('<table class="table table-hover table-bordered table-text-center"></table>')
            var thead = $('<thead><tr><th></th><th>参数名称</th><th>参数值</th><th>操作</th></tr></thead>');
            table.append(thead);
            var tbody = $('<tbody id="paramBody"></tbody>');
            $.each(apiInfo.parameters, function (i, param) {
                var tr = $('<tr></tr>');

                var checkbox = $('<td><div class="checkbox"><label><input type="checkbox" value="" checked></label></div></td>');
                var key = $('<td><input class="form-control p-key" value="' + param.name + '"/></td>')
                var value = $('<td><input class="form-control p-value" placeholder="' + DApiUI.getStringValue(param['description']) + '"/></td>');
                var oper = $('<td><button class="btn btn-danger btn-circle btn-lg" type="button"><strong>×</strong></button></td>');
                //删除事件
                oper.find("button").on("click", function (e) {
                    e.preventDefault();
                    var that = $(this);
                    that.parent().parent().remove();
                })
                tr.append(checkbox).append(key).append(value).append(oper);
                tbody.append(tr);
            })
            table.append(tbody);
            divpbody.append(table);
        } else {
            divpbody.append($('<strong>暂无参数</strong>'))
        }
        divp.append(divpbody);


        div.append(divp);

        //创建reesponsebody
        var respcleanDiv = $('<div id="responsebody"></div>');
        div.append(respcleanDiv);

        DApiUI.getDoc().find("#tab2").find(".panel-body").html("")
        DApiUI.getDoc().find("#tab2").find(".panel-body").append(div);


        //发送事件
        headdiv1.find("#btnRequest").bind("click", function (e) {
            e.preventDefault();
            respcleanDiv.html("")
            DApiUI.log("发送请求");
            //
            var params = {};

            //获取参数
            var paramBody = DApiUI.getDoc().find("#tab2").find("#paramBody")
            DApiUI.log("paramsbody..")
            DApiUI.log(paramBody)

            paramBody.find("tr").each(function () {
                var paramtr = $(this);
                var cked = paramtr.find("td:first").find(":checked").prop("checked");
                DApiUI.log(cked)
                if (cked) {
                    //获取key
                    var key = paramtr.find("td:eq(1)").find("input").val();
                    //获取value
                    var value = paramtr.find("td:eq(2)").find("input").val();
                    params[key] = value;
                    DApiUI.log("key:" + key + ",value:" + value);
                }
            })
            DApiUI.log("获取参数..")
            DApiUI.log(params);

            var basePath = null;
            if (apiInfo.basePath.startsWith('/')) {
                basePath = apiInfo.basePath;
            } else {
                basePath = '/' + apiInfo.basePath;
            }
            if (apiInfo.basePath.endsWith('/')) {
                basePath = basePath.slice(0, -1);
            }
            var data = null;
            if (apiInfo.methodType == 'post') {
                data = JSON.stringify(params);
            }else{
                data = params;
            }
            $.ajax({
                url: DApiUI.getStringValue(basePath + apiInfo.url),
                type: DApiUI.getStringValue(apiInfo.methodType),
                data: data,
                success: function (data, status, xhr) {
                    var resptab = $('<div id="resptab" class="tabs-container" ></div>')
                    var ulresp = $('<ul class="nav nav-tabs">' +
                        '<li class=""><a data-toggle="tab" href="#tabresp" aria-expanded="false"> 响应内容 </a></li>' +
                        '<li class=""><a data-toggle="tab" href="#tabcookie" aria-expanded="true"> Cookies</a></li>' +
                        '<li class=""><a data-toggle="tab" href="#tabheader" aria-expanded="true"> Headers </a></li></ul>')

                    resptab.append(ulresp);
                    var respcontent = $('<div class="tab-content"></div>');

                    var resp1 = $('<div id="tabresp" class="tab-pane active"><div class="panel-body"><pre></pre></div></div>');
                    var resp2 = $('<div id="tabcookie" class="tab-pane active"><div class="panel-body">暂无</div>');
                    var resp3 = $('<div id="tabheader" class="tab-pane active"><div class="panel-body">暂无</div></div>');

                    respcontent.append(resp1).append(resp2).append(resp3);

                    resptab.append(respcontent)

                    respcleanDiv.append(resptab);
                    DApiUI.log(xhr);
                    DApiUI.log(xhr.getAllResponseHeaders());
                    var allheaders = xhr.getAllResponseHeaders();
                    if (allheaders != null && typeof (allheaders) != 'undefined' && allheaders != "") {
                        var headers = allheaders.split("\r\n");
                        var headertable = $('<table class="table table-hover table-bordered table-text-center"><tr><th>请求头</th><th>value</th></tr></table>');
                        for (var i = 0; i < headers.length; i++) {
                            var header = headers[i];
                            if (header != null && header != "") {
                                var headerValu = header.split(":");
                                var headertr = $('<tr><th class="active">' + headerValu[0] + '</th><td>' + headerValu[1] + '</td></tr>');
                                headertable.append(headertr);
                            }
                        }
                        //设置Headers内容
                        resp3.find(".panel-body").html("")
                        resp3.find(".panel-body").append(headertable);
                    }
                    var contentType = xhr.getResponseHeader("Content-Type");
                    DApiUI.log("Content-Type:" + contentType);
                    DApiUI.log(xhr.hasOwnProperty("responseJSON"));
                    if (xhr.hasOwnProperty("responseJSON")) {
                        //如果存在该对象,服务端返回为json格式
                        resp1.find(".panel-body").html("")
                        DApiUI.log(xhr["responseJSON"])
                        var pre = $('<pre></pre>')
                        var jsondiv = $('<div></div>')
                        jsondiv.JSONView(xhr["responseJSON"]);
                        pre.html(JSON.stringify(xhr["responseJSON"], null, 2));
                        resp1.find(".panel-body").append(jsondiv);
                        //$("#headJsonDiv").show();
                        /* $("#headJsonDiv").show();
                         resp1.find(".panel-body").append($("#headJsonDiv"))
                         setTimeout(function () {
                         $("#enterValue").val(JSON.stringify(xhr["responseJSON"]));
                         console.log($("#enterValue").val())
                         console.log("click事件")
                         $("#enterOk").click();
                         }, 100)*/


                    } else {
                        //判断content-type
                        //如果是image资源
                        var regex = new RegExp('image/(jpeg|jpg|png|gif)', 'g');
                        if (regex.test(contentType)) {
                            var d = DApiUI.getDoc().data("data");
                            var imgUrl = "http://" + d.host + apiInfo.url;
                            var img = document.createElement("img");
                            img.onload = function (e) {
                                window.URL.revokeObjectURL(img.src); // 清除释放
                            };
                            img.src = imgUrl;
                            resp1.find(".panel-body").html("")
                            resp1.find(".panel-body")[0].appendChild(img);
                        } else {
                            //判断是否是text
                            var regex = new RegExp('.*?text.*', 'g');
                            if (regex.test(contentType)) {
                                resp1.find(".panel-body").html("")
                                resp1.find(".panel-body").html(xhr.responseText);
                            }
                        }

                    }

                    DApiUI.log("tab show...")
                    resptab.find("a:first").tab("show");
                },
                error: function (xhr, textStatus, errorThrown) {
                    DApiUI.log("error.....")
                    DApiUI.log(xhr);
                    DApiUI.log(textStatus);
                    DApiUI.log(errorThrown);
                    var resptab = $('<div id="resptab" class="tabs-container" ></div>')
                    var ulresp = $('<ul class="nav nav-tabs">' +
                        '<li class=""><a data-toggle="tab" href="#tabresp" aria-expanded="false"> 响应内容 </a></li>' +
                        '<li class=""><a data-toggle="tab" href="#tabcookie" aria-expanded="true"> Cookies</a></li>' +
                        '<li class=""><a data-toggle="tab" href="#tabheader" aria-expanded="true"> Headers </a></li></ul>')

                    resptab.append(ulresp);
                    var respcontent = $('<div class="tab-content"></div>');

                    var resp1 = $('<div id="tabresp" class="tab-pane active"><div class="panel-body"><pre></pre></div></div>');
                    var resp2 = $('<div id="tabcookie" class="tab-pane active"><div class="panel-body">暂无</div>');
                    var resp3 = $('<div id="tabheader" class="tab-pane active"><div class="panel-body">暂无</div></div>');

                    respcontent.append(resp1).append(resp2).append(resp3);

                    resptab.append(respcontent)

                    respcleanDiv.append(resptab);
                    DApiUI.log(xhr);
                    DApiUI.log(xhr.getAllResponseHeaders());
                    var allheaders = xhr.getAllResponseHeaders();
                    if (allheaders != null && typeof (allheaders) != 'undefined' && allheaders != "") {
                        var headers = allheaders.split("\r\n");
                        var headertable = $('<table class="table table-hover table-bordered table-text-center"><tr><th>请求头</th><th>value</th></tr></table>');
                        for (var i = 0; i < headers.length; i++) {
                            var header = headers[i];
                            if (header != null && header != "") {
                                var headerValu = header.split(":");
                                var headertr = $('<tr><th class="active">' + headerValu[0] + '</th><td>' + headerValu[1] + '</td></tr>');
                                headertable.append(headertr);
                            }
                        }
                        //设置Headers内容
                        resp3.find(".panel-body").html("")
                        resp3.find(".panel-body").append(headertable);
                    }
                    var contentType = xhr.getResponseHeader("Content-Type");
                    DApiUI.log("Content-Type:" + contentType);
                    var jsonRegex = "";
                    DApiUI.log(xhr.hasOwnProperty("responseJSON"))
                    if (xhr.hasOwnProperty("responseJSON")) {
                        //如果存在该对象,服务端返回为json格式
                        resp1.find(".panel-body").html("")
                        DApiUI.log(xhr["responseJSON"])
                        /*var pre=$('<pre></pre>')
                         pre.html(JSON.stringify(xhr["responseJSON"],null,2));*/
                        var jsondiv = $('<div></div>')
                        jsondiv.JSONView(xhr["responseJSON"]);
                        //pre.html(JSON.stringify(xhr["responseJSON"],null,2));
                        resp1.find(".panel-body").append(jsondiv);
                        //resp1.find(".panel-body").append(pre);
                    } else {
                        //判断是否是text
                        var regex = new RegExp('.*?text.*', 'g');
                        if (regex.test(contentType)) {
                            resp1.find(".panel-body").html("")
                            resp1.find(".panel-body").html(xhr.responseText);
                        }
                    }
                    DApiUI.log("tab show...")
                    resptab.find("a:first").tab("show");

                }
            })
        })

    }

    DApiUI.createDebugResponseTab = function (parent, data) {

    }


    DApiUI.writeUTF8 = function (str, isGetBytes) {
        var back = [],
            byteSize = 0;
        for (var i = 0; i < str.length; i++) {
            var code = str.charCodeAt(i);
            if (code >= 0 && code <= 127) {
                byteSize += 1;
                back.push(code);
            } else if (code >= 128 && code <= 2047) {
                byteSize += 2;
                back.push((192 | (31 & (code >> 6))));
                back.push((128 | (63 & code)))
            } else if (code >= 2048 && code <= 65535) {
                byteSize += 3;
                back.push((224 | (15 & (code >> 12))));
                back.push((128 | (63 & (code >> 6))));
                back.push((128 | (63 & code)))
            }
        }
        for (i = 0; i < back.length; i++) {
            if (back[i] > 255) {
                back[i] &= 255
            }
        }
        if (isGetBytes) {
            return back
        }
        if (byteSize <= 255) {
            return [0, byteSize].concat(back);
        } else {
            return [byteSize >> 8, byteSize & 255].concat(back);
        }
    }

    DApiUI.createApiInfoTable = function (apiInfo) {
        var table = $('<table class="table table-hover table-bordered table-text-center"></table>');
        var thead = $('<thead><tr><th colspan="2" style="text-align:center">Swagger-Bootstrap-UI-前后端api接口文档</th></tr></thead>');
        table.append(thead);
        var tbody = $('<tbody></tbody>');

        var url = $('<tr><th class="active" style="text-align: right;">接口url</th><td style="text-align: left"><code>' + DApiUI.getStringValue(apiInfo.url) + '</code></td></tr>');
        tbody.append(url);

        var summary = $('<tr><th class="active" style="text-align: right;">接口名称</th><td style="text-align: left">' + DApiUI.getStringValue(apiInfo.summary) + '</td></tr>');
        tbody.append(summary);


        var description = $('<tr><th class="active" style="text-align: right;">说明</th><td style="text-align: left">' + DApiUI.getStringValue(apiInfo.description) + '</td></tr>');
        tbody.append(description);

        var methodType = $('<tr><th class="active" style="text-align: right;">请求方式</th><td style="text-align: left"><code>' + DApiUI.getStringValue(apiInfo.methodType) + '</code></td></tr>');
        tbody.append(methodType);


        var consumes = $('<tr><th class="active" style="text-align: right;">consumes</th><td style="text-align: left"><code>' + apiInfo.consumes.join(",") + '</code></td></tr>');
        tbody.append(consumes);

        var produces = $('<tr><th class="active" style="text-align: right;">produces</th><td style="text-align: left"><code>' + apiInfo.produces.join(",") + '</code></td></tr>');
        tbody.append(produces);

        //请求参数
        var args = $('<tr><th class="active" style="text-align: right;">请求参数</th></tr>');
        //判断是否有请求参数
        if (typeof (apiInfo.parameters) != 'undefined' && apiInfo.parameters != null) {
            var ptd = $("<td></td>");
            var ptable = $('<table class="table table-bordered"></table>')
            var phead = $('<thead><th>参数名称</th><th>说明</th><th>类型</th><th>in</th><th>是否必须</th></thead>');
            ptable.append(phead);
            var pbody = $('<tbody></tbody>');
            $.each(apiInfo.parameters, function (i, param) {
                var ptr = $('<tr><td>' + param.name + '</td><td>' + DApiUI.getStringValue(param['description']) + '</td><td>' + DApiUI.getDefaultRequiredType(param['type']) + '</td><td>' + DApiUI.getStringValue(param['in']) + '</td><td>' + param['required'] + '</td></tr>');
                pbody.append(ptr);
            })
            ptable.append(pbody);
            ptd.append(ptable);
            args.append(ptd);
        } else {
            args.append($("<td>暂无</td>"));
        }
        tbody.append(args);

        //响应状态码
        var response = $('<tr><th class="active" style="text-align: right;">响应</th></tr>');
        if (typeof (apiInfo.responses) != 'undefined' && apiInfo.responses != null) {
            var resp = apiInfo.responses;
            var ptd = $("<td></td>");
            var ptable = $('<table class="table table-bordered"></table>')
            var phead = $('<thead><th>状态码</th><th>说明</th><th>schema</th></thead>');
            ptable.append(phead);
            var pbody = $('<tbody></tbody>');
            if (resp.hasOwnProperty("200")) {
                var ptr = $('<tr><td>200</td><td>http响应成功</td><td></td></tr>');
                pbody.append(ptr);
            }
            //400
            pbody.append($('<tr><td>400</td><td>Bad Request 请求出现语法错误,一般是请求参数不对</td><td></td></tr>'));
            //404
            pbody.append($('<tr><td>404</td><td>Not Found 无法找到指定位置的资源</td><td></td></tr>'));
            //401
            pbody.append($('<tr><td>401</td><td>Unauthorized 访问被拒绝</td><td></td></tr>'));
            //403
            pbody.append($('<tr><td>403</td><td>Forbidden 资源不可用</td><td></td></tr>'));
            //500
            pbody.append($('<tr><td>500</td><td>服务器内部错误,请联系Java后台开发人员!!!</td><td></td></tr>'));
            ptable.append(pbody);
            ptd.append(ptable);
            response.append(ptd);
        } else {
            response.append($("<td>暂无</td>"));
        }
        tbody.append(response);
        table.append(tbody);

        DApiUI.creatabTab();
        //内容覆盖
        //DApiUI.getDoc().html("");
        //查找接口doc
        DApiUI.getDoc().find("#tab1").find(".panel-body").html("")
        DApiUI.getDoc().find("#tab1").find(".panel-body").append(table);
        //DApiUI.getDoc().append(table);

    }


    /***
     * 获取默认请求参数类型
     * @param obj
     * @returns {string}
     */
    DApiUI.getDefaultRequiredType = function (obj) {
        var t = "string";
        if (typeof (obj) != 'undefined' && obj != null) {
            t = obj.toString();
        }
        return t;
    }

    /***
     * 查找子类
     * @param tagInfo
     * @param menu
     */
    DApiUI.initChildrens = function (tagInfo, menu) {

    }

    DApiUI.getDoc = function () {
        return $("#content");
    }
    DApiUI.getMenu = function () {
        return $("#menu");
    }

    DApiUI.log = function (msg) {
        if (window.console) {
            console.log(msg);
        }
    }
    DApiUI.init();


    /***
     * 标签组信息
     * @constructor
     */
    function TagInfo(name, description) {
        this.name = name;
        this.description = description;
        this.childrens = new Array();
    }


    /***
     * api实体信息
     * @param options
     * @constructor
     */
    function ApiInfo(options) {
        //判断options
        this.tag = "";
        this.url = "";
        this.description = "";
        this.operationId = "";
        this.parameters = new Array();
        this.produces = new Array();
        this.responses = {};
        this.methodType = "post";
        this.consumes = new Array();
        this.summary = "";
        if (options != null && typeof (options) != 'undefined') {
            this.tag = options.tags[0];
            this.description = options.description;
            this.operationId = options.operationId;
            this.summary = options.summary;
            this.parameters = options.parameters;
            this.produces = options.produces;
            this.responses = options.responses;
            this.consumes = options.consumes;
            this.basePath = options.basePath;
        }

    }


})