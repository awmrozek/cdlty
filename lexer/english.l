/* English -> American */
%%
"colour" { printf("color"); }
"flavour" { printf("flavor"); }
"clever" { printf("smart"); }
"smart" { printf("liberal"); }
"conservative" { printf("liberal"); }
. { printf("%s", yytext); }
%%
