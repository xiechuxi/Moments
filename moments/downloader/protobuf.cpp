syntax = "proto3";
 
package bilibili.community.service.dm.v1;

//弹幕
service DM {
    // 获取分段弹幕
    rpc DmSegMobile(DmSegMobileReq) returns(DmSegMobileReply);
    // 客户端弹幕元数据 字幕、分段、防挡蒙版等
    rpc DmView(DmViewReq) returns(DmViewReply);
    // 修改弹幕配置
    rpc DmPlayerConfig(DmPlayerConfigReq) returns(Response);
    // ott弹幕列表
    rpc DmSegOtt(DmSegOttReq) returns(DmSegOttReply);
    // SDK弹幕列表
    rpc DmSegSDK(DmSegSDKReq) returns(DmSegSDKReply);
    //
    rpc DmExpoReport(DmExpoReportReq) returns(DmExpoReportRes);
}

//
message BuzzwordConfig {
    //
    repeated BuzzwordShowConfig keywords = 1;
}

//
message BuzzwordShowConfig {
    //
    string name = 1;
    //
    string schema = 2;
    //
    int32 source = 3;
    //
    int64 id = 4;
    //
    int64 buzzword_id = 5;
    //
    int32 schema_type = 6;
}

// 互动弹幕条目信息
message CommandDm {
    // 弹幕id
    int64 id = 1;
    // 对象视频cid
    int64 oid = 2;
    // 发送者mid
    string mid = 3;
    // 互动弹幕指令
    string command = 4;
    // 互动弹幕正文
    string content = 5;
    // 出现时间
    int32 progress = 6;
    // 创建时间
    string ctime = 7;
    // 发布时间
    string mtime = 8;
    // 扩展json数据
    string extra = 9;
    // 弹幕id str类型
    string idStr = 10;
}

// 弹幕属性位值
enum DMAttrBit {
    DMAttrBitProtect = 0;  // 保护弹幕
    DMAttrBitFromLive = 1; // 直播弹幕
    DMAttrHighLike = 2;    // 高赞弹幕
}

// 弹幕ai云屏蔽列表
message DanmakuAIFlag {
    // 弹幕ai云屏蔽条目
    repeated DanmakuFlag dm_flags = 1;
}

// 弹幕条目
message DanmakuElem {
    // 弹幕dmid
    int64 id = 1;
    // 弹幕出现位置(单位ms)
    int32 progress = 2;
    // 弹幕类型
    int32 mode = 3;
    // 弹幕字号
    int32 fontsize = 4;
    // 弹幕颜色
    uint32 color = 5;
    // 发送着mid hash
    string midHash = 6;
    // 弹幕正文
    string content = 7;
    // 发送时间
    int64 ctime = 8;
    // 权重 区间:[1,10]
    int32 weight = 9;
    // 动作
    string action = 10;
    // 弹幕池
    int32 pool = 11;
    // 弹幕dmid str
    string idStr = 12;
    // 弹幕属性位(bin求AND)
    // bit0:保护 bit1:直播 bit2:高赞
    int32 attr = 13;
}

// 弹幕ai云屏蔽条目
message DanmakuFlag {
    int64 dmid = 1;  // 弹幕dmid
    uint32 flag = 2; // 评分
}

// 云屏蔽配置信息
message DanmakuFlagConfig {
    // 云屏蔽等级
    int32 rec_flag = 1;
    // 云屏蔽文案
    string rec_text = 2;
    // 云屏蔽开关
    int32 rec_switch = 3;
}

// 弹幕默认配置
message DanmuDefaultPlayerConfig {
    bool player_danmaku_use_default_config = 1;    // 是否使用推荐弹幕设置
    bool player_danmaku_ai_recommended_switch = 4; // 是否开启智能云屏蔽
    int32 player_danmaku_ai_recommended_level = 5; // 智能云屏蔽等级
    bool player_danmaku_blocktop = 6;              // 是否屏蔽顶端弹幕
    bool player_danmaku_blockscroll = 7;           // 是否屏蔽滚动弹幕
    bool player_danmaku_blockbottom = 8;           // 是否屏蔽底端弹幕
    bool player_danmaku_blockcolorful = 9;         // 是否屏蔽彩色弹幕
    bool player_danmaku_blockrepeat = 10;          // 是否屏蔽重复弹幕
    bool player_danmaku_blockspecial = 11;         // 是否屏蔽高级弹幕
    float player_danmaku_opacity = 12;             // 弹幕不透明度
    float player_danmaku_scalingfactor = 13;       // 弹幕缩放比例
    float player_danmaku_domain = 14;              // 弹幕显示区域
    int32 player_danmaku_speed = 15;               // 弹幕速度
    bool inline_player_danmaku_switch = 16;        // 是否开启弹幕
    int32 player_danmaku_senior_mode_switch = 17;  //
}

// 弹幕配置
message DanmuPlayerConfig {
    bool player_danmaku_switch = 1;                // 是否开启弹幕
    bool player_danmaku_switch_save = 2;           // 是否记录弹幕开关设置
    bool player_danmaku_use_default_config = 3;    // 是否使用推荐弹幕设置
    bool player_danmaku_ai_recommended_switch = 4; // 是否开启智能云屏蔽
    int32 player_danmaku_ai_recommended_level = 5; // 智能云屏蔽等级
    bool player_danmaku_blocktop = 6;              // 是否屏蔽顶端弹幕
    bool player_danmaku_blockscroll = 7;           // 是否屏蔽滚动弹幕
    bool player_danmaku_blockbottom = 8;           // 是否屏蔽底端弹幕
    bool player_danmaku_blockcolorful = 9;         // 是否屏蔽彩色弹幕
    bool player_danmaku_blockrepeat = 10;          // 是否屏蔽重复弹幕
    bool player_danmaku_blockspecial = 11;         // 是否屏蔽高级弹幕
    float player_danmaku_opacity = 12;             // 弹幕不透明度
    float player_danmaku_scalingfactor = 13;       // 弹幕缩放比例
    float player_danmaku_domain = 14;              // 弹幕显示区域
    int32 player_danmaku_speed = 15;               // 弹幕速度
    bool player_danmaku_enableblocklist = 16;      // 是否开启屏蔽列表
    bool inline_player_danmaku_switch = 17;        // 是否开启弹幕
    int32 inline_player_danmaku_config = 18;       //
    int32 player_danmaku_ios_switch_save = 19;     //
    int32 player_danmaku_senior_mode_switch = 20;  //
}

// 弹幕显示区域自动配置
message DanmuPlayerDynamicConfig {
    // 时间
    int32 progress = 1;
    // 弹幕显示区域
    float player_danmaku_domain = 14;
}

// 弹幕配置信息
message DanmuPlayerViewConfig {
    // 弹幕默认配置
    DanmuDefaultPlayerConfig danmuku_default_player_config = 1;
    // 弹幕用户配置
    DanmuPlayerConfig danmuku_player_config = 2;
    // 弹幕显示区域自动配置列表
    repeated DanmuPlayerDynamicConfig danmuku_player_dynamic_config = 3;
}

// web端用户弹幕配置
message DanmuWebPlayerConfig {
    bool dm_switch = 1;            // 是否开启弹幕
    bool ai_switch = 2;            // 是否开启智能云屏蔽
    int32 ai_level = 3;            // 智能云屏蔽等级
    bool blocktop = 4;             // 是否屏蔽顶端弹幕
    bool blockscroll = 5;          // 是否屏蔽滚动弹幕
    bool blockbottom = 6;          // 是否屏蔽底端弹幕
    bool blockcolor = 7;           // 是否屏蔽彩色弹幕
    bool blockspecial = 8;         // 是否屏蔽重复弹幕
    bool preventshade = 9;         // 
    bool dmask = 10;               // 
    float opacity = 11;            // 
    int32 dmarea = 12;             // 
    float speedplus = 13;          // 
    float fontsize = 14;           // 弹幕字号
    bool screensync = 15;          // 
    bool speedsync = 16;           // 
    string fontfamily = 17;        // 
    bool bold = 18;                // 是否使用加粗
    int32 fontborder = 19;         // 
    string draw_type = 20;         // 弹幕渲染类型
    int32 senior_mode_switch = 21; //
}

//
message DmExpoReportReq {
    //
    string session_id = 1;
    //
    int64 oid = 2;
    //
    string spmid = 4;
}

//
message DmExpoReportRes {

}

// 修改弹幕配置-请求
message DmPlayerConfigReq {
    int64 ts = 1;                                               //
    PlayerDanmakuSwitch switch = 2;                             // 是否开启弹幕
    PlayerDanmakuSwitchSave switch_save = 3;                    // 是否记录弹幕开关设置
    PlayerDanmakuUseDefaultConfig use_default_config = 4;       // 是否使用推荐弹幕设置
    PlayerDanmakuAiRecommendedSwitch ai_recommended_switch = 5; // 是否开启智能云屏蔽
    PlayerDanmakuAiRecommendedLevel ai_recommended_level = 6;   // 智能云屏蔽等级
    PlayerDanmakuBlocktop blocktop = 7;                         // 是否屏蔽顶端弹幕
    PlayerDanmakuBlockscroll blockscroll = 8;                   // 是否屏蔽滚动弹幕
    PlayerDanmakuBlockbottom blockbottom = 9;                   // 是否屏蔽底端弹幕
    PlayerDanmakuBlockcolorful blockcolorful = 10;              // 是否屏蔽彩色弹幕
    PlayerDanmakuBlockrepeat blockrepeat = 11;                  // 是否屏蔽重复弹幕
    PlayerDanmakuBlockspecial blockspecial = 12;                // 是否屏蔽高级弹幕
    PlayerDanmakuOpacity opacity = 13;                          // 弹幕不透明度
    PlayerDanmakuScalingfactor scalingfactor = 14;              // 弹幕缩放比例
    PlayerDanmakuDomain domain = 15;                            // 弹幕显示区域
    PlayerDanmakuSpeed speed = 16;                              // 弹幕速度
    PlayerDanmakuEnableblocklist enableblocklist = 17;          // 是否开启屏蔽列表
    InlinePlayerDanmakuSwitch inlinePlayerDanmakuSwitch = 18;   // 是否开启弹幕
    PlayerDanmakuSeniorModeSwitch senior_mode_switch = 19;      //
}

//
message DmSegConfig {
    //
    int64 page_size = 1;
    //
    int64 total = 2;
}

// 获取弹幕-响应
message DmSegMobileReply {
    // 弹幕列表
    repeated DanmakuElem elems = 1;
    // 是否已关闭弹幕
    // 0:未关闭 1:已关闭
    int32 state = 2;
    // 弹幕云屏蔽ai评分值
    DanmakuAIFlag ai_flag = 3;
}

// 获取弹幕-请求
message DmSegMobileReq {
    // 稿件avid/漫画epid
    int64 pid = 1;
    // 视频cid/漫画cid
    int64 oid = 2;
    // 弹幕类型
    // 1:视频 2:漫画
    int32 type = 3;
    // 分段(6min)
    int64 segment_index = 4;
    // 是否青少年模式
    int32 teenagers_mode = 5;
}

// ott弹幕列表-响应
message DmSegOttReply {
    // 是否已关闭弹幕
    // 0:未关闭 1:已关闭
    bool closed = 1;
    // 弹幕列表
    repeated DanmakuElem elems = 2;
}

// ott弹幕列表-请求
message DmSegOttReq {
    // 稿件avid/漫画epid
    int64 pid = 1;
    // 视频cid/漫画cid
    int64 oid = 2;
    // 弹幕类型
    // 1:视频 2:漫画
    int32 type = 3;
    // 分段(6min)
    int64 segment_index = 4;
}

// 弹幕SDK-响应
message DmSegSDKReply {
    // 是否已关闭弹幕
    // 0:未关闭 1:已关闭
    bool closed = 1;
    // 弹幕列表
    repeated DanmakuElem elems = 2;
}

// 弹幕SDK-请求
message DmSegSDKReq {
    // 稿件avid/漫画epid
    int64 pid = 1;
    // 视频cid/漫画cid
    int64 oid = 2;
    // 弹幕类型
    // 1:视频 2:漫画
    int32 type = 3;
    // 分段(6min)
    int64 segment_index = 4;
}

// 客户端弹幕元数据-响应
message DmViewReply {
    // 是否已关闭弹幕
    // 0:未关闭 1:已关闭
    bool closed = 1;
    // 智能防挡弹幕蒙版信息
    VideoMask mask = 2;
    // 视频字幕
    VideoSubtitle subtitle = 3;
    // 高级弹幕专包url(bfs)
    repeated string special_dms = 4;
    // 云屏蔽配置信息
    DanmakuFlagConfig ai_flag = 5;
    // 弹幕配置信息
    DanmuPlayerViewConfig player_config = 6;
    // 弹幕发送框样式
    int32 send_box_style = 7;
    // 是否允许
    bool allow = 8;
    // check box 是否展示
    string check_box = 9;
    // check box 展示文本
    string check_box_show_msg = 10;
    // 展示文案
    string text_placeholder = 11;
    // 弹幕输入框文案
    string input_placeholder = 12;
    // 用户举报弹幕 cid维度屏蔽的正则规则
    repeated string report_filter_content = 13;
    //
    ExpoReport expo_report = 14;
    //
    BuzzwordConfig buzzword_config = 15;
    //
    repeated Expressions expressions = 16;
}

// 客户端弹幕元数据-请求
message DmViewReq {
    // 稿件avid/漫画epid
    int64 pid = 1;
    // 视频cid/漫画cid
    int64 oid = 2;
    // 弹幕类型
    // 1:视频 2:漫画
    int32 type = 3;
    // 页面spm
    string spmid = 4;
    // 是否冷启
    int32 is_hard_boot = 5;
}

// web端弹幕元数据-响应
message DmWebViewReply {
    // 是否已关闭弹幕
    // 0:未关闭 1:已关闭
    int32 state = 1;
    //
    string text = 2;
    //
    string text_side = 3;
    // 分段弹幕配置
    DmSegConfig dm_sge = 4;
    // 云屏蔽配置信息
    DanmakuFlagConfig flag = 5;
    // 高级弹幕专包url(bfs)
    repeated string special_dms = 6;
    // check box 是否展示
    bool check_box = 7;
    // 弹幕数
    int64 count = 8;
    // 互动弹幕
    repeated CommandDm commandDms = 9;
    // 用户弹幕配置
    DanmuWebPlayerConfig player_config = 10;
    // 用户举报弹幕 cid维度屏蔽
    repeated string report_filter_content = 11;
    //
    repeated Expressions expressions = 12;
}

//
message ExpoReport {
    //
    bool should_report_at_end = 1;
}

//
message Expression {
    //
    repeated string keyword = 1;
    //
    string url = 2;
    //
    repeated Period period = 3;
}

//
message Expressions {
    //
    repeated Expression data = 1;
}

//
message Period {
    //
    int64 start = 1;
    //
    int64 end = 2;
}

// 是否开启弹幕
message InlinePlayerDanmakuSwitch {bool value = 1; }
// 智能云屏蔽等级
message PlayerDanmakuAiRecommendedLevel {bool value = 1; }
// 是否开启智能云屏蔽
message PlayerDanmakuAiRecommendedSwitch {bool value = 1; }
// 是否屏蔽底端弹幕
message PlayerDanmakuBlockbottom {bool value = 1; }
// 是否屏蔽彩色弹幕
message PlayerDanmakuBlockcolorful {bool value = 1; }
// 是否屏蔽重复弹幕
message PlayerDanmakuBlockrepeat {bool value = 1; }
// 是否屏蔽滚动弹幕
message PlayerDanmakuBlockscroll {bool value = 1; }
// 是否屏蔽高级弹幕
message PlayerDanmakuBlockspecial {bool value = 1; }
// 是否屏蔽顶端弹幕
message PlayerDanmakuBlocktop {bool value = 1; }
// 弹幕显示区域
message PlayerDanmakuDomain {float value = 1; }
// 是否开启屏蔽列表
message PlayerDanmakuEnableblocklist {bool value = 1; }
// 弹幕不透明度
message PlayerDanmakuOpacity {float value = 1; }
// 弹幕缩放比例
message PlayerDanmakuScalingfactor {float value = 1; }
//
message PlayerDanmakuSeniorModeSwitch {int32 value = 1; }
// 弹幕速度
message PlayerDanmakuSpeed {int32 value = 1; }
// 是否开启弹幕
message PlayerDanmakuSwitch {bool value = 1;bool canIgnore = 2; }
// 是否记录弹幕开关设置
message PlayerDanmakuSwitchSave {bool value = 1; }
// 是否使用推荐弹幕设置
message PlayerDanmakuUseDefaultConfig {bool value = 1; }

// 修改弹幕配置-响应
message Response {
    //
    int32 code = 1;
    //
    string message = 2;
}

// 单个字幕信息
message SubtitleItem {
    // 字幕id
    int64 id = 1;
    // 字幕id str
    string id_str = 2;
    // 字幕语言代码
    string lan = 3;
    // 字幕语言
    string lan_doc = 4;
    // 字幕文件url
    string subtitle_url = 5;
    // 字幕作者信息
    UserInfo author = 6;
    // 字幕类型
    SubtitleType type = 7;
}

enum SubtitleType {
    CC = 0; // CC字幕
    AI = 1; // AI生成字幕
}

// 字幕作者信息
message UserInfo {
    // 用户mid
    int64 mid = 1;
    // 用户昵称
    string name = 2;
    // 用户性别
    string sex = 3;
    // 用户头像url
    string face = 4;
    // 用户签名
    string sign = 5;
    // 用户等级
    int32 rank = 6;
}

// 智能防挡弹幕蒙版信息
message VideoMask {
    // 视频cid
    int64 cid = 1;
    // 平台
    // 0:web端 1:客户端
    int32 plat = 2;
    // 帧率
    int32 fps = 3;
    // 间隔时间
    int64 time = 4;
    // 蒙版url
    string mask_url = 5;
}

// 视频字幕信息
message VideoSubtitle {
    // 视频原语言代码
    string lan = 1;
    // 视频原语言
    string lanDoc = 2;
    // 视频字幕列表
    repeated SubtitleItem subtitles = 3;
}