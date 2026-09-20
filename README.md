# Shadowrocket 远程更新配置

这个仓库模板用于托管 Shadowrocket 基础配置，并在每周日北京时间 10:23 自动同步、净化应用广告模块。

## 一次性部署

1. 在 GitHub 新建一个公开仓库，例如 `shadowrocket-rules`。
2. 将本模板解压后的全部内容上传到仓库 `main` 分支，包括 `.github`、`dist` 和 `scripts`。
3. 打开仓库的 `Actions` 页面，允许运行工作流。
4. 运行一次 `Update Shadowrocket rules`，确认执行成功。
5. 仓库若禁止 Actions 写入，请在 `Settings > Actions > General > Workflow permissions` 选择 `Read and write permissions`。

## Shadowrocket 导入地址

基础配置：

```text
https://raw.githubusercontent.com/haokun-1/shadowrocket-rules/main/dist/Shadowrocket_CN_Direct_AdBlock.conf
```

广告模块：

```text
https://raw.githubusercontent.com/haokun-1/shadowrocket-rules/main/dist/Shadowrocket_CN_Apps_AdBlock_730.srmodule
```

在 Shadowrocket 的“配置”页面通过 URL 下载基础配置；在“配置 > 模块”页面通过 URL 添加广告模块。第一次导入后不需要反复安装证书或节点，后续在相应列表中下拉更新即可。

## 更新机制

- 基础配置内部的广告、分流和 HTTPDNS 列表本身就是远程 URL。
- GitHub Actions 每周日北京时间 10:23 执行一次 `scripts/update_rules.py`，同步上游应用净化模块。
- 更新脚本会移除会员状态修改、Spotify 破解及远程覆盖地址，保留广告拦截和页面净化规则。
- 也可以在 GitHub `Actions` 页面手动运行工作流，随后在 Shadowrocket 中刷新模块。

## 使用要求

- iPhone 上的 Shadowrocket 全局路由设为“配置”。
- 启用广告模块和 HTTPS 解密。
- Shadowrocket CA 证书必须安装并在 iOS 中完全信任。
- 仓库必须公开，否则 Shadowrocket 无法在未登录 GitHub 的情况下读取 Raw URL。
