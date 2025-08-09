if vim.g.vscode then
  require("vsconfig.autocmds")
  require("vsconfig.options")
else
  -- bootstrap lazy.nvim, LazyVim and your plugins
  require("config.lazy")
  require("config.template")
  vim.o.tabstop = 4
  vim.bo.tabstop = 4
  vim.o.softtabstop = 4
  vim.o.shiftround = true
  vim.o.shiftwidth = 4
  -- vim.o.background = "light"
  --vim.o.updatetime = 6000 require("config.template")
end

local theme = os.getenv("TERTHEME")
if theme == "dark" then
  vim.o.background = "dark"
else
  vim.o.background = "light"
end
