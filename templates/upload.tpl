{% extends "base.tpl" %}

{% block title %}Upload{% end %}

{% block body %}

<form action="" method="POST" enctype="multipart/form-data">
  <label>Project: {{proj}} </label>
  <input type="file" name="file"/>
  <input type="submit" value="Upload"/>
</form>
{% end %}

