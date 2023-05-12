        return redirect(
            reverse("app1_product_master:cart_list")+'?'+urlencode({"quote_id":quote_id, "node":node})
        )
